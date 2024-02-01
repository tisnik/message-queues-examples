import time

import zmq

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_server():
    """Spuštění serveru."""
    context = zmq.Context()

    try:
        socket = context.socket(CONNECTION_TYPE)
        address = "tcp://*:{port}".format(port=PORT)
        socket.bind(address)
        try:
            print("Bound to address {a}".format(a=address))

            for i in range(10):
                send_message(socket, "Message #{i}".format(i=i))
                time.sleep(1)
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


start_server()
