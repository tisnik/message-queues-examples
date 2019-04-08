package main

import (
	streaming "github.com/nats-io/go-nats-streaming"
	"log"
)

const clusterId = "test-cluster"
const clientId = "consumer1"
const topic = "topic1"

func onReceive(m *streaming.Msg) {
	println("Received message: ", string(m.Data))
}

func main() {
	stream, err := streaming.Connect(clusterId, clientId)
	if err != nil {
		log.Fatalf("Can not connect to cluster %s\n", clusterId)
	}
	defer stream.Close()

	c := make(chan bool)

	// jeste jednou ziska posledni zpravu zpracovanou minule
	startOpt := streaming.StartWithLastReceived()
	sub, err := stream.Subscribe(topic, onReceive, startOpt)
	if err != nil {
		log.Fatalf("Can not subscribe to topic %s\n", topic)
	}
	defer sub.Unsubscribe()

	<-c
}
