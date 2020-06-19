package main

import (
	"fmt"
	"github.com/Shopify/sarama"
)

func main() {
	broker := sarama.NewBroker("localhost:9092")
	err := broker.Open(nil)
	if err != nil {
		panic(err)
	}

	request := sarama.MetadataRequest{Topics: []string{"myTopic"}}
	response, err := broker.GetMetadata(&request)
	if err != nil {
		_ = broker.Close()
		panic(err)
	}

	fmt.Println("There are", len(response.Topics), "topics active in the cluster.")

	if err = broker.Close(); err != nil {
		panic(err)
	}

	consumer, err := sarama.NewConsumer([]string{"localhost:9092"}, nil)
	if err != nil {
		panic(err)
	}

	defer func() {
		if err := consumer.Close(); err != nil {
			panic(err)
		}
	}()

	partitionConsumer, err := consumer.ConsumePartition("platform.results.ccx", 0, sarama.OffsetNewest)
	if err != nil {
		panic(err)
	}

	defer func() {
		if err := partitionConsumer.Close(); err != nil {
			panic(err)
		}
	}()

	// Trap SIGINT to trigger a shutdown.
	//signals := make(chan os.Signal, 1)
	//signal.Notify(signals, os.Interrupt)

	consumed := 0
	for {
		msg := <-partitionConsumer.Messages()
		fmt.Printf("Consumed message offset %d\n", msg.Offset)
		consumed++
	}

	fmt.Printf("Consumed: %d\n", consumed)
}
