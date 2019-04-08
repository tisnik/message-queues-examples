package main

import streaming "github.com/nats-io/go-nats-streaming"

const clusterId = "test-cluster"
const clientId = "publisher1"
const topic = "topic1"

func main() {
	stream, _ := streaming.Connect(clusterId, clientId)

	stream.Publish(topic, []byte("Hello World"))

	stream.Close()
}
