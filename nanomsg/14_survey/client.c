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

void receive_question(const int socket)
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

void send_answer(const int socket, const char *answer)
{
    int bytes;

    printf("Sending answer '%s'\n", answer);
    if ((bytes = nn_send(socket, answer, strlen(answer)+1, 0)) < 0) {
        report_error("nn_send");
    }
    printf("Answer with length %d bytes sent, flushing\n", bytes);
}

#define ANSWER_LENGTH 100

void client(const char *url)
{
    int socket;
    int endpoint;
    char answer[ANSWER_LENGTH];
    int number;

    if ((socket = nn_socket(AF_SP, NN_RESPONDENT)) < 0) {
        report_error("nn_socket");
    }
    puts("Socket created");

    if ((endpoint = nn_connect(socket, url)) < 0) {
        report_error("nn_connect");
    }
    puts("Remote endpoint added to the socket");

    while (1) {
        receive_question(socket);
        puts("Question received");

        /* nemame vypocetni vykon Hlubiny mysleni... */
        srand((unsigned) getpid());
        number = rand() % 100;

        snprintf(answer, ANSWER_LENGTH, "It must be %d", number);
        send_answer(socket, answer);
        puts("Answer sent");
    }

    if (nn_shutdown(socket, endpoint) < 0) {
        report_error("nn_shutdown");
    }
    puts("Shutdown completed");
}

int main(const int argc, const char **argv)
{
    client(URL);
    return 0;
}
