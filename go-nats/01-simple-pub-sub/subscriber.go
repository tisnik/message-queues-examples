package main

import (
	"fmt"
	nats "github.com/nats-io/go-nats"
	"sync"
)

const Subject = "test1"

func main() {
	conn, _ := nats.Connect(nats.DefaultURL)

	wg := sync.WaitGroup{}
	wg.Add(1)

	conn.Subscribe(Subject, func(m *nats.Msg) {
		fmt.Printf("Received a message: %s\n", string(m.Data))
		wg.Done()
	})
	wg.Wait()
}
