#include <unistd.h>
#include <stdio.h>
#include <signal.h>

int x = 0;
pid_t pid;


void	sig_handler1(int sig)
{
	pid = getpid();
	printf("the PID is %d\n", pid);

}

void	sig_handler2(int sig)
{
		printf("x=%d\n", ++x);

}
void	sig_handler3(int sig)
{
		printf("x=%d\n", ++x);

}
int main()
{


	signal(SIGINT, sig_handler1); //ctr+c
	signal(SIGUSR1, sig_handler2); //SIGUSR1 = KILL -10
	signal(SIGUSR2, sig_handler3); //kill -12
	
	while(1)
		sleep(1); //wait for signals
	return (0);
}