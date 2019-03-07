package main

import (
	"encoding/json"
	"github.com/adjust/rmq"
	"time"
)

type TaskPayload struct {
	Id     int32
	Name   string
	Param1 int32
	Param2 int32
}

type Consumer struct {
}

func NewConsumer() *Consumer {
	return &Consumer{}
}

func (consumer *Consumer) Consume(delivery rmq.Delivery) {
	println("consume begin")

	println(delivery.Payload())

	var task TaskPayload
	if err := json.Unmarshal([]byte(delivery.Payload()), &task); err != nil {
		delivery.Reject()
		return
	}

	println("performing task", task.Id, "name", task.Name, "with parameters", task.Param1, task.Param2)
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
