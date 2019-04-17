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

void first(const char *url)
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

    if ((endpoint = nn_connect(socket, url)) < 0) {
        report_error("nn_connect");
    }
    puts("Remote endpoint added to the socket");

    message = "Hello from 'first'!";
    printf("Sending message '%s'\n", message);
    if ((bytes = nn_send(socket, message, strlen(message)+1, 0)) < 0) {
        report_error("nn_send");
    }

    printf("Message with length %d bytes sent, flushing\n", bytes);
    sleep(1);

    puts("Waiting for response...");
    response = NULL;
    if ((bytes = nn_recv(socket, &response, NN_MSG, 0)) < 0) {
        report_error("nn_recv");
    }
    printf("Received response '%s' with length %d bytes\n", response, bytes); 
    if (nn_freemsg(response) < 0) {
        report_error("nn_freemsg");
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(const int argc, const char **argv)
{
    first(URL);
    return 0;
}
