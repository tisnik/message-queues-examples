#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <zmq.h>

#define BUFFER_LENGTH 32

int main()
{
    char buffer[BUFFER_LENGTH];
    char *address = "tcp://localhost:5556";

    void *context = zmq_ctx_new();
    void *socket = zmq_socket(context, ZMQ_PAIR);

    zmq_connect(socket, address);
    printf("Connected to address %s\n", address);

    while (1)
    {
        int num = zmq_recv(socket, buffer, BUFFER_LENGTH-1, 0);
        buffer[num] = '\0';
        printf("Received '%s'\n", buffer);
    }

    zmq_close(socket);
    zmq_ctx_destroy(context);

    return 0;
}

