#include <signal.h>
#include <unistd.h>
#include <stdio.h>


int	g_sig;

void sig_handler_usr2()
{
	printf("SIGUSR2 is called\n");
}
void sig_handler_usr1()
{
	printf("SIGUSR1 is called\n");
}

int main()
{
	while (1)
	{
		sleep(5);
		printf("on running PID(%d)\n", getpid());
		signal(SIGUSR1, sig_handler_usr1);
		signal(SIGUSR2, sig_handler_usr2);

	}

}