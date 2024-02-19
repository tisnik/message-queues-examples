import tornado.ioloop

import nsq

cnt = 1


def pub_message():
    global cnt
    writer.pub("test", "zprava {}".format(cnt).encode(), finish_pub)
    cnt += 1


def finish_pub(conn, data):
    print("FINISHING")
    print(data.decode())
    print("---------")


writer = nsq.Writer(["127.0.0.1:4150"])

tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
