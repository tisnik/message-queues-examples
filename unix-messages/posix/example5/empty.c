/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue5"

int main(void)
{
    mqd_t message_queue_id;
    unsigned int sender;
    char message_text[10000];
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDONLY | O_NONBLOCK);
    if (message_queue_id == -1) {
        perror("Unable to get queue");
        return 2;
    }

    while (1) {
        status = mq_receive(message_queue_id, message_text, sizeof(message_text), &sender);
        if (status == -1) {
            if (errno == EAGAIN) {
                puts("Message queue is empty...");
                break;
            }
            perror("Unable to receive message");
            return 2;
        }
        printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);
    }

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
