#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <zmq.h>

#define BUFFER_LENGTH 32
#define BUFFER2_LENGTH (32 + sizeof("Acknowledge: "))

int main()
{
    char buffer[BUFFER_LENGTH];
    char buffer2[BUFFER_LENGTH];
    char *address = "tcp://localhost:5556";
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

    rc = zmq_connect(socket, address);

    if (rc != 0) {
        perror("cannot connect()");
        zmq_close(socket);
        zmq_ctx_destroy(context);
        return -1;
    }
    printf("Connected to address %s\n", address);

    while (1)
    {
        int num = zmq_recv(socket, buffer, BUFFER_LENGTH-1, 0);
        if (num < 0) {
            perror("zmq_recv() failed");
        }
        else {
            buffer[num] = '\0';
            printf("Received '%s'\n", buffer);

            snprintf(buffer2, BUFFER2_LENGTH, "Acknowledge: %s", buffer);
            num = zmq_send(socket, buffer2, strlen(buffer2), 0);
            if (num < 0) {
                perror("zmq_send() failed");
            }
        }
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

