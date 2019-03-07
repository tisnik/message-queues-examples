package main

import (
	"github.com/adjust/rmq"
	"io/ioutil"
)

func SendBinaryMessage(binaryMessagesQueue rmq.Queue, binaryMessage []byte) {
	binaryMessagesQueue.PublishBytes(binaryMessage)
}

func SendFileContent(binaryMessagesQueue rmq.Queue, filename string) {
	bytes, err := ioutil.ReadFile(filename)
	if err == nil {
		println("Read", len(bytes), "bytes")
		SendBinaryMessage(binaryMessagesQueue, bytes)
		println("Sent")
	} else {
		println("Error opening file", err)
	}
}

func main() {
	connection := rmq.OpenConnection("binary_message_app", "tcp", "localhost:6379", 1)
	println("Connection object: ", connection)

	binaryMessagesQueue := connection.OpenQueue("binary_messages_queue")
	println("Queue: ", binaryMessagesQueue)

	SendFileContent(binaryMessagesQueue, "vim_editor.gif")
}
