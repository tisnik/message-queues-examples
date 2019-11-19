#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue1"

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
