### sigaction()

 give more options how you handle your signal than signal()


 ### SIGUSR

 user-defined signal for custom behaviors
reserved for user-defined purpose in Unix-like OS

 ## SIGUSR1, SIGUSR2
 -generally, SIRUSR1 = 10, SIRUSR2 = 12, these can vary btw systems

  ### code
#include <signal.h>

printf("SIGUSR1: %d\n", SIGUSR1);
printf("SIGUSR2: %d\n", SIGUSR2);

### SIGSTOP


### SIGCONT

 continue if stopped