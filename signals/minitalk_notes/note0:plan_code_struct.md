### last checklist
1. norm : *.c, Makefile, *.h

## to test
https://www.codequoi.com/en/sending-and-intercepting-a-signal-in-c/
https://github.com/xicodomingues/francinette //tester on mac
- mem leak
- send 5000 chars
- send multiple msgs
- client uses only SIGUSR1, 2
- server uses only SIGUSR1, s

### assignment(pdf)

server 
	must started 1st
	after its launch -> print its PID
	receive STR -> print STR

client
	takes 2 parameters(server PID, STR to send)
	send STR

Communication
	Displaying / speed
	: 1 sec for 100 chars is way too much/slow

	done only using UNIX signals
	: not queue signals
	
	can only use these two signals : SIGUSR1, SIGUSR2

## instruction
# must
Makefile : must
hadle error : must
	(quit unexpectedly, seg fault, bus err, double free, and so on): not allowed
handle mem, leak : MUST

# allowed
ur libft : allowed
one global var for server, one for client : allowed, but have to justify its use

## allowed funct
write, ft_printf, 
signal, sigemptyset, sigaddset, sigaction
kill, getpid
malloc, free
pause, sleep, uslepp
exit

## bonus part

server acknowledges every msg by sendiing back a sig to the client
unicode chars support



### what to do

pass str of chars from one pro to another
using kill() with SIGUSR1/2
	(1) pass data in binary form

using sleep() or usleep()
	(2) wait to receive the ctrl bit
	* depends on OS


### good to know

code working on linux might not work on MacOS

### two main 

in client.c
in serer.c

## server.c
void handle_signal(int sig)

int main()
	//get PID
	//set up sig handlers
	//infinite loop to wait for signals
	return 0

## client.c
void send_bit(pid_t server_pid, int bit)

int	main(int ac, char *av[])
	if (ac == 2)
		//handle error
	pid_t server_pid = atoi(argv[1])
	//get msg to send
	//send each bit to server

	return 0
	

