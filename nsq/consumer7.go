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

	config := nsq.NewConfig()

	for i := 0; i <= 1; i++ {
		consumer, err := nsq.NewConsumer(Topic, Channel, config)
		if err != nil {
			log.Panic("Consumer can't be constructed")
		}
		consumer.AddHandler(nsq.HandlerFunc(func(message *nsq.Message) error {
			log.Printf("Received a message from nsqd #%d: %s", i+1, string(message.Body))
			return nil
		}))
		err = consumer.ConnectToNSQD(os.Args[i+1])
		if err != nil {
			log.Panicf("Could not connect to nsqd #%d", i)
		}
	}

	log.Println("Waiting for message")
	done := make(chan bool)

	<-done
}
