package main

import (
	"github.com/nsqio/go-nsq"
	"log"
)

const Address = "127.0.0.1:4150"

const Topic = "test"

const Channel = "B"

func main() {
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

	err = consumer.ConnectToNSQD(Address)
	if err != nil {
		log.Panic("Could not connect")
	}

	log.Println("Waiting for message")
	<-done
}
