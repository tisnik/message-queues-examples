package main

import (
	nats "github.com/nats-io/go-nats"
	"log"
)

const Subject = "test1"
const Queue = "q1"

func main() {
	conn, err := nats.Connect(nats.DefaultURL)

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	econn, err2 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)

	if err2 != nil {
		log.Fatal(err2)
	}

	defer econn.Close()

	channel := make(chan string)
	econn.BindRecvQueueChan(Subject, Queue, channel)

	println("Channel created")

	for i := 1; i < 20; i++ {
		println(<-channel)
	}
}
