/*
 * Example used in following article:
 *
 * Fronty zpráv podle Systemu V
 * https://www.root.cz/clanky/fronty-zprav-podle-systemu-v/
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

typedef struct {
    long message_type;
    char message_text[100];
} t_message;

int main(void)
{
    t_message message;
    key_t key;
    int queue_id;
    int status;
    int msg_number = 1;

    message.message_type = 1;

    key = ftok("/home/tester/.bashrc", 1234);

    if (key == -1) {
        perror("Unable to generate key");
        return 2;
    }

    printf("Key: %x\n", key);

    queue_id = msgget(key, IPC_CREAT | 0660);

    if (queue_id == -1) {
        perror("Unable to get message queue identifier");
        return 2;
    }

    printf("Message queue identifier: %x\n", queue_id);

    while (1) {
        sprintf(message.message_text, "Message #%d", msg_number);
        msg_number++;
        status = msgsnd(queue_id, (void*)&message, sizeof(message.message_text), 0);

        if (status == -1) {
            perror("Can not send message");
            return 1;
        }
        sleep(1);
    }

    return 0;
}
