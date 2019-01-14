#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <zmq.h>

#define BUFFER_LENGTH 32
#define BUFFER2_LENGTH (32 + sizeof("Acknowledge: "))

int main()
{
    char buffer[BUFFER_LENGTH];
    char buffer2[BUFFER2_LENGTH];

    char *address = "tcp://*:5556";

    void *context = zmq_ctx_new();
    void *socket = zmq_socket(context, ZMQ_PAIR);

    zmq_bind(socket, address);
    printf("Bound to address %s\n", address);

    int i;
    for (i=0; i<10; i++)
    {
        snprintf(buffer, BUFFER_LENGTH, "Message #%d", i+1);
        printf("Sending message '%s'\n", buffer);
        zmq_send(socket, buffer, strlen(buffer), 0);

        printf("Sent, waiting for response...\n");
        int num = zmq_recv(socket, buffer2, BUFFER2_LENGTH-1, 0);
        buffer2[num] = '\0';
        printf("Received response '%s'\n", buffer2);

        sleep(1);
    }

    zmq_close(socket);
    zmq_ctx_destroy(context);

    return 0;
}
