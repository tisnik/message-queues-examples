package main

import (
	"fmt"
	"github.com/Shopify/sarama"
)

func main() {
	consumer, err := sarama.NewConsumer([]string{"localhost:9092"}, nil)
	if err != nil {
		panic(err)
	}

	defer func() {
		if err := consumer.Close(); err != nil {
			panic(err)
		}
	}()

	partitionConsumer, err := consumer.ConsumePartition("platform.upload.buckit", 0, sarama.OffsetNewest)
	if err != nil {
		panic(err)
	}

	defer func() {
		if err := partitionConsumer.Close(); err != nil {
			panic(err)
		}
	}()

	consumed := 0
	for {
		msg := <-partitionConsumer.Messages()
		fmt.Printf("Consumed message offset %d\n", msg.Offset)
		consumed++
	}

	fmt.Printf("Consumed: %d\n", consumed)
}
