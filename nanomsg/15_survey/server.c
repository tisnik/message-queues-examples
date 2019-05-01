#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <nanomsg/nn.h>
#include <nanomsg/survey.h>

const char *URL = "ipc:///tmp/example14";

void report_error(const char *func)
{
    fprintf(stderr, "%s: %s\n", func, nn_strerror(nn_errno()));
    exit(1);
}

void send_survey(const int socket, const char *message)
{
    int bytes;

    printf("Sending message '%s'\n", message);
    if ((bytes = nn_send(socket, message, strlen(message)+1, 0)) < 0) {
        report_error("nn_send");
    }
    printf("Message with length %d bytes sent, flushing\n", bytes);
}

void receive_answer(const int socket)
{
    char *response = NULL;
    int bytes;

    if ((bytes = nn_recv(socket, &response, NN_MSG, 0)) < 0) {
        report_error("nn_recv");
    }
    printf("Received answer '%s' with length %d bytes\n", response, bytes); 
    if (nn_freemsg(response) < 0) {
        report_error("nn_freemsg");
    }
}

void wait_for_clients(int seconds)
{
    int i;
    puts("Waiting for clients to connect...");
    for (i=10; i>0; i--) {
        printf("%d  ", i);
        fflush(stdout);
        sleep(1);
    }
    puts("\nDone");
}

void server(const char *url)
{
    int socket;
    int endpoint;
    int answers;

    if ((socket = nn_socket(AF_SP, NN_SURVEYOR)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_bind(socket, url)) < 0) {
        report_error("nn_bind");
    }
    puts("Endpoint bound to socket");

    wait_for_clients(10);

    send_survey(socket, "What do you get when you multiply six by nine?");
    puts("Survey send, waiting for answers...");

    while (1) {
        receive_answer(socket);
        answers++;
        printf("Processed %d answers so far\n", answers);
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(int argc, char **argv)
{
    server(URL);
    return 0;
}
