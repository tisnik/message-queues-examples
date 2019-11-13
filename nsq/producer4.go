package main

import (
	"fmt"
	"github.com/nsqio/go-nsq"
	"log"
	"os"
	"time"
)

const Topic = "test"

func main() {
	if len(os.Args) < 2 {
		log.Panic("nsqd address needs to be specified on CLI")
	}

	address := os.Args[1]

	config := nsq.NewConfig()

	producer, err := nsq.NewProducer(address, config)
	if err != nil {
		log.Panic("Producer can't be constructed")
	}
	defer producer.Stop()

	i := 0

	for {
		message := fmt.Sprintf("Zprava z Go #%d", i)
		log.Print("Sending message: ", message)
		err = producer.Publish(Topic, []byte(message))
		if err != nil {
			log.Panic("Could not connect")
		}
		i++
		time.Sleep(1 * time.Second)
	}
}
