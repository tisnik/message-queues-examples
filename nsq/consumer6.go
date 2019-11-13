package main

import (
	"github.com/nsqio/go-nsq"
	"log"
	"os"
)

const Topic = "test"

const Channel = "A"

func main() {
	if len(os.Args) < 3 {
		log.Panic("two nsqd addresses needs to be specified on CLI")
	}

	address1 := os.Args[1]
	address2 := os.Args[2]
	config := nsq.NewConfig()

	consumer, err := nsq.NewConsumer(Topic, Channel, config)
	if err != nil {
		log.Panic("Consumer can't be constructed")
	}

	done := make(chan bool)

	consumer.AddHandler(nsq.HandlerFunc(func(message *nsq.Message) error {
		log.Printf("Received a message: %s", string(message.Body))
		// done <- true
		return nil
	}))

	err = consumer.ConnectToNSQDs([]string{address1, address2})
	if err != nil {
		log.Panic("Could not connect")
	}

	log.Println("Waiting for message")
	<-done
}
