hi:
	echo "hi world"

code1: code1.c
	cc code1.c -o code1

SRC := $(wildcard *.c)

OBJ : $(SRC:.c=.o)

%.o : %.c
	cc  -c $< -o $@

clean: 
	rm -f $(OBJ) code1