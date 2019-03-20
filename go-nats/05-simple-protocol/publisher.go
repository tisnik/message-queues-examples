package main

import (
	nats "github.com/nats-io/go-nats"
	"log"
)

const Subject = "test1"

func main() {
	conn, err := nats.Connect(nats.DefaultURL)

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	println("Connected")

	econn, err2 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)

	if err2 != nil {
		log.Fatal(err)
	}

	defer econn.Close()

	channel := make(chan string)
	econn.BindSendChan(Subject, channel)

	println("Channel created")

	channel <- "Hello World #1"
	channel <- "Hello World #2"
	channel <- "Hello World #3"
	channel <- "EXIT"

	conn.Flush()

	println("All messages sent")
}
