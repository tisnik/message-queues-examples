/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue6"

int main(void)
{
    mqd_t message_queue_id;

    struct mq_attr msgq_attr;
    msgq_attr.mq_flags = 0;
    msgq_attr.mq_maxmsg = 10;
    msgq_attr.mq_msgsize = 20;
    msgq_attr.mq_curmsgs = 1;

    mq_unlink(QUEUE_NAME);
    message_queue_id = mq_open(QUEUE_NAME, O_RDWR | O_CREAT | O_EXCL, S_IRWXU | S_IRWXG, &msgq_attr);
    if (message_queue_id == -1) {
        perror("Unable to create queue");
        return 2;
    }
    return 0;
}
