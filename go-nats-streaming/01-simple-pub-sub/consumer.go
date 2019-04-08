package main

import streaming "github.com/nats-io/go-nats-streaming"

const clusterId = "test-cluster"
const clientId = "consumer1"
const topic = "topic1"

func onReceive(m *streaming.Msg) {
	println("Received message: ", string(m.Data))
}

func main() {
	stream, _ := streaming.Connect(clusterId, clientId)

	c := make(chan bool)

	sub, _ := stream.Subscribe(topic, onReceive)

	<-c

	sub.Unsubscribe()

	stream.Close()
}
