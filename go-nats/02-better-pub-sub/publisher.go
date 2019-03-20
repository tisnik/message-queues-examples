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

	err2 := conn.Publish(Subject, []byte("Hello World"))

	if err2 != nil {
		log.Fatal(err2)
	}

	conn.Flush()

	println("Message sent")
}
