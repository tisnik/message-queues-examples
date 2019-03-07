package main

import (
	"encoding/json"
	"github.com/adjust/rmq"
)

type TaskPayload struct {
	Id     int32
	Name   string
	Param1 int32
	Param2 int32
}

func SendTask(taskQueue rmq.Queue, payload TaskPayload) {
	bytes, err := json.Marshal(payload)
	if err != nil {
		println(err)
		return
	}
	taskQueue.PublishBytes(bytes)
}

func main() {
	connection := rmq.OpenConnection("test_service_producer", "tcp", "localhost:6379", 1)
	println("Connection object: ", connection)

	taskQueue := connection.OpenQueue("task_queue")
	println("Queue: ", taskQueue)

	SendTask(taskQueue, TaskPayload{1, "test1", 0, 0})
	SendTask(taskQueue, TaskPayload{2, "test2", 6, 7})
}
