package main

import (
	"github.com/adjust/rmq"
	"io/ioutil"
	"time"
)

type Consumer struct{}

func NewConsumer() *Consumer {
	return &Consumer{}
}

func (consumer *Consumer) Consume(delivery rmq.Delivery) {
	const FileFlags = 0664

	println("consume begin")
	payload := delivery.Payload()

	println("Received binary message", len(payload), "bytes")

	err := ioutil.WriteFile("received.gif", []byte(payload), FileFlags)
	if err == nil {
		println("Written")
	} else {
		println(err)
	}
	delivery.Ack()

	println("consume end")
}

func main() {
	connection := rmq.OpenConnection("binary_messages_queue", "tcp", "localhost:6379", 1)
	println("Connection object: ", connection)

	binaryMessagesQueue := connection.OpenQueue("binary_messages_queue")
	println("Queue: ", binaryMessagesQueue)

	binaryMessagesQueue.StartConsuming(10, time.Second)
	binaryMessagesQueue.AddConsumer("consumer", NewConsumer())
	select {}
}
