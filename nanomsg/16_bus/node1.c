#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/bus.h>

const char *URL = "ipc:///tmp/example14";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void receive_message(const int socket)
{
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

void node1(const char *url)
{
    int socket;
    int endpoint;
    int messages = 0;

    if ((socket = nn_socket(AF_SP, NN_BUS)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_bind(socket, url)) < 0) {
        report_error("nn_bind");
    }
    printf("Remote endpoint %s bound to the socket\n", url);

    puts("Waiting for messages...");

    while (1) {
        receive_message(socket);
        messages++;
        printf("Processed %d messages so far\n", messages);
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(const int argc, const char **argv)
{
    node1(URL);
    return 0;
}
