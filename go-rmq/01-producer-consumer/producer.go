package main

import "github.com/adjust/rmq"

func main() {
	connection := rmq.OpenConnection("test_service_producer", "tcp", "localhost:6379", 1)
	println("Connection object: ", connection)

	taskQueue := connection.OpenQueue("task_queue")
	println("Queue: ", taskQueue)

	delivery := "task payload 1"
	taskQueue.Publish(delivery)

	delivery = "task payload 2"
	taskQueue.Publish(delivery)
}
