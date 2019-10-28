package main

import (
	"github.com/nsqio/go-nsq"
	"log"
)

func main() {
	config := nsq.NewConfig()

	consumer, err := nsq.NewConsumer("test", "test", config)
	if err != nil {
		log.Panic("Consumer can't be constructed")
	}

	done := make(chan bool)

	consumer.AddHandler(nsq.HandlerFunc(func(message *nsq.Message) error {
		log.Printf("Received a message: %s", string(message.Body))
		return nil
	}))

	err = consumer.ConnectToNSQLookupd("127.0.0.1:4161")
	if err != nil {
		log.Panic("Could not connect")
	}
	defer consumer.DisconnectFromNSQLookupd("127.0.0.1:4150")

	log.Println("Waiting for message")
	<-done
}
