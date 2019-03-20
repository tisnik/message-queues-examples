package main

import (
	nats "github.com/nats-io/go-nats"
	"log"
	"time"
)

const Subject = "test1"
const Control = "test2"

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

	cconn, err3 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)

	if err3 != nil {
		log.Fatal(err3)
	}

	defer cconn.Close()

	data_channel := make(chan string)
	econn.BindSendChan(Subject, data_channel)

	println("Data channel created")

	control_channel := make(chan string)
	cconn.BindSendChan(Control, control_channel)

	println("Control channel created")

	data_channel <- "Hello World #1"
	data_channel <- "Hello World #2"
	data_channel <- "Hello World #3"
	data_channel <- "EXIT"
	time.Sleep(2 * time.Second)
	control_channel <- "EXIT"

	conn.Flush()

	println("All messages sent")
}
