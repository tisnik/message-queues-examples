#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/pair.h>

const char *URL = "ipc:///tmp/example3";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void second(const char *url)
{
    int socket;
    int endpoint;
    int bytes;
    char *message = NULL;
    char *response = NULL;

    if ((socket = nn_socket(AF_SP, NN_PAIR)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_bind(socket, url)) < 0) {
        report_error("nn_bind");
    }
    puts("Endpoint bound to socket");

    puts("Waiting for message...");
    if ((bytes = nn_recv(socket, &message, NN_MSG, 0)) < 0) {
        report_error("nn_recv");
    }
    printf("Received message '%s' with length %d bytes\n", message, bytes); 
    if (nn_freemsg(message) < 0) {
        report_error("nn_freemsg");
    }

    response = "ACK!";

    printf("Sending response '%s'\n", response);
    if ((bytes = nn_send(socket, response, strlen(response)+1, 0)) < 0) {
        report_error("nn_send");
    }

    printf("Response with length %d bytes sent, flushing\n", bytes);
    sleep(1);

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(int argc, char **argv)
{
    second(URL);
    return 0;
}
