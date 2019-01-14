#include <stdio.h>
#include <zmq.h>

int main()
{
    void *context = zmq_ctx_new();
    void *socket = zmq_socket(context, ZMQ_PAIR);

    printf("%p\n", context);
    printf("%p\n", socket);

    zmq_close(socket);
    zmq_ctx_destroy(context);

    return 0;
}

