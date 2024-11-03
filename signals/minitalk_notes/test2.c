#include <unistd.h> //fork(), sleep()

int main()
{
	int pid = fork();

	if (pid == -1)
		return 1;
	if (pid == 0)
	{
		while (1)
		{
			printf("on running\n");
			usleep(50000);
		}
	}
	else
	{
		kill(pid, SIGKILL);
		wait(1);
	}
	return (0);
}