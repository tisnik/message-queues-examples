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
    int rc;

    void *context = zmq_ctx_new();

    if (context == NULL) {
        perror("zmq_ctx_new() failed");
        return -1;
    }

    void *socket = zmq_socket(context, ZMQ_PAIR);

    if (socket == NULL) {
        perror("zmq_socket() failed");
        zmq_ctx_destroy(context);
        return -1;
    }

    rc = zmq_bind(socket, address);
    if (rc != 0) {
        perror("cannot bind()");
        zmq_close(socket);
        zmq_ctx_destroy(context);
        return -1;
    }
    printf("Bound to address %s\n", address);

    int i;
    for (i=0; i<10; i++)
    {
        snprintf(buffer, BUFFER_LENGTH, "Message #%d", i+1);
        printf("Sending message '%s'\n", buffer);
        rc = zmq_send(socket, buffer, strlen(buffer), 0);
        if (rc < 0) {
            perror("zmq_send() failed");
        }

        printf("Sent, waiting for response...\n");
        int num = zmq_recv(socket, buffer2, BUFFER2_LENGTH-1, 0);
        if (num < 0) {
            perror("zmq_recv() failed");
        }
        else {
            buffer2[num] = '\0';
            printf("Received response '%s'\n", buffer2);
        }

        sleep(1);
    }

    rc = zmq_close(socket);

    if (rc != 0) {
        perror("cannot close socket");
        zmq_ctx_destroy(context);
        return -1;
    }

    rc = zmq_ctx_destroy(context);

    if (rc != 0) {
        perror("zmq_ctx_destroy() failed");
        return -1;
    }

    return 0;
}

