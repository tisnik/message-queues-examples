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

	econn, err2 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)

	if err2 != nil {
		log.Fatal(err)
	}

	defer econn.Close()

	channel := make(chan string)
	econn.BindRecvChan(Subject, channel)

	println("Channel created")

	for {
		message := <-channel
		println(message)
		if message == "EXIT" {
			println("Received EXIT message...")
			break
		}
	}
}
