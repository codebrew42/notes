#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

volatile sig_atomic_t stop = 0;

void handle_sigint(int sig) 
{
    stop = 1; // Set the stop flag when SIGINT is received
}

int main() {
    signal(SIGINT, handle_sigint); // Register the SIGINT handler

    while (!stop) {
        // Simulate server activity (e.g., waiting for messages)
        printf("Server running... Press Ctrl+C to stop.\n");
        sleep(2); // Sleep for a while to simulate work
    }

    printf("Server shutting down...\n");
    return 0;
}
