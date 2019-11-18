#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

typedef struct {
    long message_type;
    char message_text[100];
} t_message;

int main(int argc, char **argv)
{
    t_message message;
    key_t key;
    int queue_id;
    int status;
    long message_type;

    if (argc < 1) {
        puts("Usage: ./subscriber message_type");
        return 1;
    }

    message_type = atoi(argv[1]);

    key = ftok("/home/tester/.bashrc", 5678);

    if (key == -1) {
        perror("Unable to generate key");
        return 2;
    }

    printf("Key: %x\n", key);

    queue_id = msgget(key, 0);

    if (queue_id == -1) {
        perror("Unable to get message queue identifier");
        return 2;
    }

    printf("Message queue identifier: %x\n", queue_id);

    while (1) {
        status = msgrcv(queue_id, (void*)&message, sizeof(message.message_text), message_type, 0);

        if (status == -1) {
            perror("Can not receive message");
            return 1;
        }

        printf("Message type: %ld\n", message.message_type);
        printf("Message text: %s\n", message.message_text);
    }
    return 0;
}
