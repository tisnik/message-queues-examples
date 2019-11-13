package main

import (
	"github.com/nsqio/go-nsq"
	"log"
	"os"
)

const Topic = "test"

const Channel = "A"

func main() {
	if len(os.Args) < 2 {
		log.Panic("nsqd address needs to be specified on CLI")
	}

	address := os.Args[1]
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

	err = consumer.ConnectToNSQD(address)
	if err != nil {
		log.Panic("Could not connect")
	}

	log.Println("Waiting for message")
	<-done
}
