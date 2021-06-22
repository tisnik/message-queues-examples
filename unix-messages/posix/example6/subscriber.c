/*
 * Example used in following article:
 *
 * Implementace front zpráv podle normy POSIX
 * https://www.root.cz/clanky/implementace-front-zprav-podle-normy-posix/
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <pthread.h>
#include <unistd.h>
#include <signal.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue6"

void register_signal(mqd_t message_queue_id);

mqd_t message_queue_id;

static void on_message(union sigval sv)
{
    unsigned int sender;
    struct mq_attr msgq_attr;

    char *message_text;
    int status;
    long message_size;

    puts("On message...");
    if (mq_getattr(message_queue_id, &msgq_attr) == -1) {
        perror("Can not read message queue attributes");
    }

    message_size = msgq_attr.mq_msgsize;
    message_text = malloc(message_size * sizeof(char));
    if (message_text == NULL) {
        perror("Allocation error");
    }

    status = mq_receive(message_queue_id, message_text, message_size, &sender);
    if (status == -1) {
        perror("Unable to receive message");
        exit(2);
    }
    printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);
    free(message_text);
    register_signal(message_queue_id);
}

void register_signal(mqd_t message_queue_id)
{
    struct sigevent sev;
    mqd_t mqdes;

    sev.sigev_notify = SIGEV_THREAD;
    sev.sigev_notify_function = on_message;
    sev.sigev_notify_attributes = NULL;
    sev.sigev_value.sival_ptr = &mqdes;

    if (mq_notify(message_queue_id, &sev) == -1)
    {
        perror("Unable to register event");
    }
    else
    {
        puts("Handler has been registered");
    }
}

int main(void)
{
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDONLY);
    if (message_queue_id == -1) {
        perror("Unable to open queue");
        return 2;
    }

    register_signal(message_queue_id);

    pause();

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
