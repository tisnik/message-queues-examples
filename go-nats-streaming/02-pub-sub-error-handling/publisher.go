package main

import (
	streaming "github.com/nats-io/go-nats-streaming"
	"log"
)

const clusterId = "test-cluster"
const clientId = "publisher1"
const topic = "topic1"

func main() {
	stream, err := streaming.Connect(clusterId, clientId)
	if err != nil {
		log.Fatalf("Can not connect to cluster %s\n", clusterId)
	}
	defer stream.Close()

	err = stream.Publish(topic, []byte("Hello World"))
	if err != nil {
		log.Fatalf("Error during publish: %v\n", err)
	} else {
		log.Println("Message published")
	}
}
