package main

import (
	nats "github.com/nats-io/go-nats"
	"log"
)

const Subject = "test1"
const Control = "test2"

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

	cconn, err3 := nats.NewEncodedConn(conn, nats.DEFAULT_ENCODER)

	if err3 != nil {
		log.Fatal(err3)
	}

	defer cconn.Close()

	data_channel := make(chan string)
	econn.BindRecvChan(Subject, data_channel)

	println("Data channel created")

	control_channel := make(chan string)
	cconn.BindRecvChan(Control, control_channel)

	println("Control channel created")

MESSAGE_LOOP:
	for {
		select {
		case message := <-data_channel:
			println("Received data message", message)
		case control := <-control_channel:
			println("Received control message", control)
			if control == "EXIT" {
				break MESSAGE_LOOP
			}
		}
		println("--------")
	}
}
