### fork

#include <unistd.h>
int main()
{
	int pid = fork();

	if (pid < 0)
	{
		perror ("for failed");
		return 1;
	}
	else if (pid == 0)
		printf("I'm child proc with PID (%d)\n", getpid());
	else
		printf("I'm parent proc with PID(%d)
		and my child proc's PID(%d)\n", getpid(), pid);
	return (0);
}

## basic
fork() creates a new proc(child) by duplicating calling proc.
returns diff val in the par/child proc
for concurrent execution -> improve efficiency/performance
=> meaning? multiple proc(tasks) running at the same time, maybe doing diff things independently

getpid() retrieves PID of cur proc
always ret PID of proc that calls int
for identifying the proc

## return
in the parent proc -> ret (PID of the child proc)
in the child proc -> ret (0)
if err -> ret (-1)

