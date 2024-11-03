## PID : process ID 

# getpid()
- <unistd.h>
-returns PID of the calling process
-purposes : logging, debugging, managing processes

# sleep(NBR)
- <unistd.h>
-purpose: to pause executin of the prog for NBR-seconds

# example

int main()
{
	while (1)
	{
		printf("wasting your (%d) cycles\n", getpid());
		sleep(1);
	}
}
-sleep() suspends executioon of calling thread for 1 sec.
-pauses for 1 sec in each iteration of loop
-> you see the output every 1 sec.

-the higher the NBR is, likely to get higer 'pid'
-if you observe total CPU cycles over a longer period, 
it might seem that sleep(3) "uses more cycles," 
but in reality, the CPU is simply idle longer between messages. 
+ If you want to measure CPU usage,
'top' or 'htop' will show that the CPU is not being actively used during the sleep periods.

- If getpid() returns 404225, 
=the current process has the process ID (PID) of 404225.
 This PID is a unique identifier assigned by the os 
 to your running process.


## how to find PID of the running program?

open terminal, 
'ps aux | grep your_program_name' on terminal/ash

## write
Value: STDOUT_FILENO is usually equal to 1. In the context of file descriptors:

0 is for standard input (stdin).
1 is for standard output (stdout).
2 is for standard error (stderr).

# example

write(STDOUT_FILENO, message, 14);
= write(1, message, 14);

## kill(pid, SIGKILL)
- <signal.h>
- kill
+ killall(kill by name), pkill(kill based on patterns)
  xkill(allows to click a window to kill), trap(catches signals in shell scripts)

# SIGKILL
-a signal telling OS to terminate a the child proc identified by PID

int main()
{

	while ()
		printf()
}

-here: printf() = child proc, will be stoopped without any chance to clean up or handle the termination gracefully

-can't be caught, blocked, ignored by proc
-forces proc to stop running right away

# basics
run the pro './a.out'
open a new terminal (any directory) -> using PID can kill or do anything

doesn't necessarily kill the proc, 
but send the signal to a proc
the proc receives the signal knows what to do.(i.e. terminate itself or whatever)

kill terminates seperately : child, parents
<=> killall terminates .a.out at once


# purpose
to terminate proc
or to send other types of signals

# example
kill -KILL 39290
=kill -9 39290


# bash script example
#!/bin/bash
kill -9 39290

# c example
-----
#include <signal.h>
#include <unistd.h> 
#include <stdio.h> //printf

int main()
{
	kill(39290, SIGKILL);
	retrun 0;
}
-----
int main()
{
	pid_t  pid = getpid();

	if (kill(pid, 0) == 0) //check if a proc with pid running
		printf("process (%d) is running\n", pid);
	else
		perror("Process killed or doesn't exist");
	return 0;
}
-----

## killall

(new terminal) killall a.out  -> even without PID

## (sig - write) why not (sig - printf) ?

printf might cause probl. crash...


### kill -l
: list all signal names and their corresponding nbrs

c3a10c1% kill -l
HUP INT QUIT ILL TRAP IOT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
                                   9    10        12

: or "man 7 signal" -> manual page