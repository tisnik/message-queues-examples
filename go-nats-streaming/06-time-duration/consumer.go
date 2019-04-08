package main

import (
	streaming "github.com/nats-io/go-nats-streaming"
	"log"
	"os"
	"time"
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

	ago := "5m"
	timeDelta, err := time.ParseDuration(ago)
	if err != nil {
		log.Fatalf("Unable to parse duration '%s'", ago)
		os.Exit(-1)
	}
	println("About to receive all messages newer than", timeDelta)

	startOpt := streaming.StartAtTimeDelta(timeDelta)
	sub, err := stream.Subscribe(topic, onReceive, startOpt)
	if err != nil {
		log.Fatalf("Can not subscribe to topic %s\n", topic)
	}
	defer sub.Unsubscribe()

	<-c
}
