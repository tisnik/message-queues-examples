package main

import (
	"github.com/nsqio/go-nsq"
	"log"
	"sync"
)

func main() {
	config := nsq.NewConfig()

	consumer, err := nsq.NewConsumer("test", "test", config)
	if err != nil {
		log.Panic("Consumer can't be constructed")
	}

	waitgroup := &sync.WaitGroup{}
	waitgroup.Add(1)

	consumer.AddHandler(nsq.HandlerFunc(func(message *nsq.Message) error {
		log.Printf("Received a message: %s", string(message.Body))
		waitgroup.Done()
		return nil
	}))

	err = consumer.ConnectToNSQD("127.0.0.1:4150")
	if err != nil {
		log.Panic("Could not connect")
	}

	log.Println("Waiting for message")
	waitgroup.Wait()
}
