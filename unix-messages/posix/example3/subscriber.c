/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue3"

int main(void)
{
    mqd_t message_queue_id;
    char message_text[10000];
    unsigned int sender;
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDWR);
    if (message_queue_id == -1) {
        perror("Unable to open queue");
        return 2;
    }

    {
        struct mq_attr msgq_attr;
        mq_getattr(message_queue_id, &msgq_attr);
        printf("Queue \"%s\":\n\t- stores at most %ld messages\n\t- large at most %ld bytes each\n\t- currently holds %ld messages\n", QUEUE_NAME, msgq_attr.mq_maxmsg, msgq_attr.mq_msgsize, msgq_attr.mq_curmsgs);
    }

    status = mq_receive(message_queue_id, message_text, sizeof(message_text), &sender);
    if (status == -1) {
        perror("Unable to receive message");
        return 2;
    }
    printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
