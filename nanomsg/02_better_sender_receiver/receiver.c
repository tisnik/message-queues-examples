#include <stdlib.h>
#include <stdio.h>
#include <nanomsg/nn.h>
#include <nanomsg/pipeline.h>

const char *URL = "ipc:///tmp/example2";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void receiver(const char *url)
{
    int socket;
    int endpoint;

    if ((socket = nn_socket(AF_SP, NN_PULL)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_bind(socket, url)) < 0) {
        report_error("nn_bind");
    }
    puts("Endpoint bound to socket");

    puts("Waiting for messages...");
    while (1) {
        char *message = NULL;
        int bytes;
        if ((bytes = nn_recv(socket, &message, NN_MSG, 0)) < 0) {
            report_error("nn_recv");
        }
        printf("Received message '%s' with length %d bytes\n", message, bytes); 
        if (nn_freemsg(message) < 0) {
            report_error("nn_freemsg");
        }
    }
}

int main(int argc, char **argv)
{
    receiver(URL);
    return 0;
}
