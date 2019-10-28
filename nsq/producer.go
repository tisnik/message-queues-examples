package main

import (
	"github.com/nsqio/go-nsq"
	"log"
)

func main() {
	config := nsq.NewConfig()

	producer, err := nsq.NewProducer("127.0.0.1:4150", config)
	if err != nil {
		log.Panic("Producer can't be constructed")
	}

	err = producer.Publish("test", []byte("zprava z Go"))
	if err != nil {
		log.Panic("Could not connect")
	}

	producer.Stop()
}
