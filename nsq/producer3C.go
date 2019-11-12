package main

import (
	"fmt"
	"github.com/nsqio/go-nsq"
	"log"
	"time"
)

const Address = "127.0.0.1:4150"

const Topic = "test"

func main() {
	config := nsq.NewConfig()

	producer, err := nsq.NewProducer(Address, config)
	if err != nil {
		log.Panic("Producer can't be constructed")
	}
	defer producer.Stop()

	i := 0

	for {
		message := fmt.Sprintf("Message from Go #%d", i)
		log.Print("Sending message: ", message)
		err = producer.Publish(Topic, []byte(message))
		if err != nil {
			log.Panic("Could not connect")
		}
		i++
		time.Sleep(300 * time.Microsecond)
	}
}
