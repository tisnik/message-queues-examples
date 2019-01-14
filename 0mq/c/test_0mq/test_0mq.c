#include <stdio.h>
#include <zmq.h>

int main()
{
    int major, minor, patch;
    void *context;
    void *socket;

    zmq_version (&major, &minor, &patch);
    printf("ØMQ version %d.%d.%d\n", major, minor, patch);

    context = zmq_ctx_new();
    socket = zmq_socket(context, ZMQ_PAIR);

    printf("%p\n", context);
    printf("%p\n", socket);

    zmq_close(socket);
    zmq_ctx_destroy(context);

    return 0;
}

