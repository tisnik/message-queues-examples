#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/pipeline.h>

const char *URL = "ipc:///tmp/example1";

void sender(const char *url, const char *message)
{
    int message_size = strlen(message) + 1;
    int socket;
    int endpoint;
    int bytes;

    socket = nn_socket(AF_SP, NN_PUSH);
    puts("Socket created");

    endpoint = nn_connect(socket, url);
    puts("Remote endpoint added to the socket");

    printf("Sending message '%s'\n", message);
    bytes = nn_send(socket, message, message_size, 0);

    printf("Message with length %d bytes sent, flushing", bytes);
    sleep(1);
    puts("Done");

    nn_shutdown(socket, endpoint);
}

int main(const int argc, const char **argv)
{
    sender(URL, "Hello");
    sender(URL, "world");
    sender(URL, "!");

    return 0;
}
