import asyncio
import nats

URL = "192.168.1.34:44853"
NATS_USERNAME = "local"
NATS_PASSWORD = "--password--"

SUBJECT_NAME = "bar"


async def on_message(message):
    print(f"Received message {message}")
    await message.ack()


async def main():
    print(f"Connecting to NATS at address {URL}")
    nats_connection = await nats.connect(URL, user=NATS_USERNAME, password=NATS_PASSWORD)
    print("Connected...")

    print("Retrieving JetStream object")
    jet_stream = nats_connection.jetstream()
    print(f"Retrieved {jet_stream}")

    print("Waiting for messages")
    sub = await jet_stream.subscribe(SUBJECT_NAME, cb=on_message)
    while True:
        await sub.next_msg(timeout=1)

    print("Closing connection")
    await nats_connection.close()
    print("Connection closed")


if __name__ == '__main__':
    asyncio.run(main())