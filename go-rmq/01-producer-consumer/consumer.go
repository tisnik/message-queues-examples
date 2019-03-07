package main

import (
	"github.com/adjust/rmq"
	"time"
)

type Consumer struct {
}

func NewConsumer() *Consumer {
	return &Consumer{}
}

func (consumer *Consumer) Consume(delivery rmq.Delivery) {
	println("consume begin")

	println(delivery.Payload())
	delivery.Ack()

	println("consume end")
}

func main() {
	connection := rmq.OpenConnection("test_service_consumer", "tcp", "localhost:6379", 1)
	println("Connection object: ", connection)

	taskQueue := connection.OpenQueue("task_queue")
	println("Queue: ", taskQueue)

	taskQueue.StartConsuming(10, time.Second)
	taskQueue.AddConsumer("consumer", NewConsumer())
	select {}
}
