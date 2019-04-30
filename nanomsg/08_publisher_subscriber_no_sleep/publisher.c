#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <nanomsg/nn.h>
#include <nanomsg/pubsub.h>

const int MAX_MESSAGES = 1000;

const char *URL = "ipc:///tmp/example8";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void send_message(const int socket, const char *message)
{
    int bytes;

    printf("Sending message '%s'\n", message);
    if ((bytes = nn_send(socket, message, strlen(message)+1, 0)) < 0) {
        report_error("nn_send");
    }
    printf("Message with length %d bytes sent, flushing\n", bytes);
}

void publisher(const char *url)
{
    int socket;
    int endpoint;
    int i;

    if ((socket = nn_socket(AF_SP, NN_PUB)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_bind(socket, url)) < 0) {
        report_error("nn_bind");
    }
    puts("Remote endpoint bound to the socket");

    for (i=0; i < MAX_MESSAGES; i++) {
        char buffer[45];
        int number = rand() % 10000;
        sprintf(buffer, "Hello, this is my top secret PIN: %04d", number);
        send_message(socket, buffer);
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(const int argc, const char **argv)
{
    publisher(URL);
    return 0;
}
