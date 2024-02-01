import zmq

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def start_client():
    """Spuštění klienta."""
    context = zmq.Context()

    try:
        socket = context.socket(CONNECTION_TYPE)
        address = "tcp://localhost:{port}".format(port=PORT)
        socket.connect(address)
        try:
            print("Connected to {a}".format(a=address))

            print("Waiting for message...")
            while True:
                message = socket.recv_string()
                print("Received message '{m}'".format(m=message))
        except Exception as e:
            print(e)
        finally:
            print("Closing socket")
            socket.close()
            print("Closed")
    except Exception as e:
        print(e)
    finally:
        print("Terminating context")
        context.term()
        print("Terminated")


start_client()
