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

void send_message(const int socket, const char *message)
{
    int bytes;

    printf("Sending message '%s'\n", message);
    if ((bytes = nn_send(socket, message, strlen(message)+1, 0)) < 0) {
        report_error("nn_send");
    }
    printf("Message with length %d bytes sent, flushing\n", bytes);
    sleep(1);
}

#define BUF_LEN 100

void node2(const char *url)
{
    int socket;
    int endpoint;
    char buffer[BUF_LEN];
    int i;

    if ((socket = nn_socket(AF_SP, NN_BUS)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    endpoint = nn_connect(socket, url);
    if (endpoint < 0) {
        report_error("nn_connect");
    }
    printf("Connected to the remote %s endpoint\n", url);
    sleep(1);

    for (i=0; i<10; i++) {
        sprintf(buffer, "Message #%d from node2", i);
        send_message(socket, buffer);
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(const int argc, const char **argv)
{
    node2(URL);
    return 0;
}
