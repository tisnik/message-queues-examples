package main

import (
	"fmt"
	nats "github.com/nats-io/go-nats"
	"log"
	"sync"
)

const Subject = "test1"

func main() {
	conn, err := nats.Connect(nats.DefaultURL)

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	wg := sync.WaitGroup{}
	wg.Add(5)

	sub, err2 := conn.Subscribe(Subject, func(m *nats.Msg) {
		fmt.Printf("Received a message: %s\n", string(m.Data))
		wg.Done()
	})

	if err2 != nil {
		log.Fatal(err2)
	}

	println("Subscribed", sub)

	err3 := sub.AutoUnsubscribe(5)

	if err3 != nil {
		log.Fatal(err3)
	}

	println("Automatic unsubscribe after 5 messages")

	wg.Wait()

	println("Finished waiting for messages")
}
