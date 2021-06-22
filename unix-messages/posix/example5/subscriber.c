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

#define QUEUE_NAME "/queue5"

mqd_t message_queue_id;

static void on_message(union sigval sv)
{
    unsigned int sender;
    char message_text[10000];
    int status;

    puts("On message...");

    status = mq_receive(message_queue_id, message_text, sizeof(message_text), &sender);
    if (status == -1) {
        perror("Unable to receive message");
        exit(2);
    }
    printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);
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
