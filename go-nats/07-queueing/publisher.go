package main

import (
	"fmt"
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
		log.Fatal(err2)
	}

	defer econn.Close()

	channel := make(chan string)
	econn.BindSendChan(Subject, channel)

	println("Channel created")

	// poslat 100 zprav
	for i := 1; i < 100; i++ {
		message := fmt.Sprintf("Hello World #%d", i)
		channel <- message
		conn.Flush()
	}

	println("All messages sent")
}
