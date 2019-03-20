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

	for i := 1; i < 10; i++ {
		message := fmt.Sprintf("Hello World #%d", i)
		err2 := conn.Publish(Subject, []byte(message))
		println("Published", message)

		if err2 != nil {
			log.Fatal(err2)
		}

		conn.Flush()
	}

	println("All messages sent")
}
