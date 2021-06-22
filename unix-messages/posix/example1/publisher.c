/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue1"

int main(void)
{
    mqd_t message_queue_id;
    unsigned int priority = 0;
    char message_text[100];
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDWR | O_CREAT | O_EXCL, S_IRWXU | S_IRWXG, NULL);
    if (message_queue_id == -1) {
        perror("Unable to create queue");
        return 2;
    }

    strcpy(message_text, "Hello world!");

    status = mq_send(message_queue_id, message_text, strlen(message_text)+1, priority);
    if (status == -1) {
        perror("Unable to send message");
        return 2;
    }

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
