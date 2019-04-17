#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/pipeline.h>

const char *URL = "ipc:///tmp/example2";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void sender(const char *url, const char *message)
{
    int message_size = strlen(message) + 1;
    int socket;
    int endpoint;
    int bytes;

    if ((socket = nn_socket(AF_SP, NN_PUSH)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_connect(socket, url)) < 0) {
        report_error("nn_connect");
    }
    puts("Remote endpoint added to the socket");

    printf("Sending message '%s'\n", message);
    if ((bytes = nn_send(socket, message, message_size, 0)) < 0) {
        report_error("nn_send");
    }

    printf("Message with length %d bytes sent, flushing", bytes);
    sleep(1);
    puts("Done");

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
}

int main(const int argc, const char **argv)
{
    sender(URL, "Hello");
    sender(URL, "world");
    sender(URL, "!");

    return 0;
}
