#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // Simulate sending messages to the server
    for (int i = 0; i < 5; i++) {
        printf("Client sending message %d\n", i + 1);
        sleep(1); // Sleep to simulate time between messages
    }

    printf("Client finished sending messages.\n");
    return 0;
}
