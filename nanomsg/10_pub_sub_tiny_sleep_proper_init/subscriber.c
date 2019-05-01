#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/pubsub.h>

const char *URL = "ipc:///tmp/example9";

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

void subscriber(const char *url)
{
    int socket;
    int endpoint;
    int messages;

    if ((socket = nn_socket(AF_SP, NN_SUB)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if (nn_setsockopt(socket, NN_SUB, NN_SUB_SUBSCRIBE, "", 0) < 0) {
        report_error("nn_setsockopt");
    }

    if ((endpoint = nn_connect(socket, url)) < 0) {
        report_error("nn_connect");
    }
    puts("Endpoint connected to socket");

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

int main(int argc, char **argv)
{
    subscriber(URL);
    return 0;
}
