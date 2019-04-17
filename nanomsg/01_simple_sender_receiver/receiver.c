#include <stdio.h>
#include <nanomsg/nn.h>
#include <nanomsg/pipeline.h>

const char *URL = "ipc:///tmp/example1";

void receiver(const char *url)
{
    int socket;

    socket = nn_socket(AF_SP, NN_PULL);
    puts("Socket created");

    nn_bind(socket, url);
    puts("Endpoint bound to socket");

    puts("Waiting for messages...");
    while (1) {
        char *message = NULL;
        int bytes = nn_recv(socket, &message, NN_MSG, 0);
        printf("Received message '%s' with length %d bytes\n", message, bytes); 
        nn_freemsg(message);
    }
}

int main(int argc, char **argv)
{
    receiver(URL);
    return 0;
}
