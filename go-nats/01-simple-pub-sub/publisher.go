package main

import nats "github.com/nats-io/go-nats"

const Subject = "test1"

func main() {
	conn, _ := nats.Connect(nats.DefaultURL)

	conn.Publish(Subject, []byte("Hello World"))

	conn.Flush()
}
