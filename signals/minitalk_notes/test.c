#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void handler(int n) 
{
    write(STDOUT_FILENO, "Received SIGINT!\n", 17);
}

void terminate(int n) 
{
    write(STDOUT_FILENO, "Terminating...\n", 16);
    exit(0);
}

void segfault_msg(int n) 
{
    write(STDERR_FILENO, "Segmentation fault!\n", 20);
}

int main() 
{
    int pid = fork();  // Create a child process

    if (pid < 0) {
        perror("fork failed");
        return 1; // Error handling
    }

    if (pid == 0) {
        // This block executes in the child process
        while (1) {
            printf("Child process with PID(%d) is running\n", getpid());
            sleep(3);  // Child sleeps for 3 seconds before printing again
        }
    } else {
        // This block executes in the parent process
        signal(SIGINT, handler); 
        signal(SIGTERM, terminate);
        signal(SIGSEGV, segfault_msg);
        
        while (1) {
            printf("Parent process with PID(%d) is running\n", getpid());
            sleep(5);  // Parent sleeps for 5 seconds before printing again
        }
    }

    return 0;
}


/*
Child Process:
The child process runs its own loop, 
printing a message every 3 seconds.

Parent Process:

The parent process has signal handlers set up for SIGINT, SIGTERM, and SIGSEGV.
 It prints its own message every 5 seconds.

*/
