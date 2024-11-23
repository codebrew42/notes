CC				:= gcc
CFLAGS			:= -Wall -Wextra -Werror


SRCS			:= a_code.c		b_code.c		c_code.c
OBJS			:= a_code.o		b_code.o		c_code.o
OBJ_A			:= a_code.o
OBJ_B			:= b_code.o
OBJ_C			:= c_code.o

TARGET_1		:= target_ab
TARGET_2		:= target_ac
TARGET_3		:= target_abc

all : $(TARGET_1) $(TARGET_2) $(TARGET_3)

# gcc -Wall -Wextra -Werror -o target1 A.o B.o
# this will compile A.o B.o into an executable named target1

#-c : .c into .o
%.o : %.c
	$(CC) $(CFLAGS) -c  $< -o $@

$(TARGET_1) : $(OBJ_A) $(OBJ_B)
	$(CC) $(CFLAGS) -o $@ $^

$(TARGET_2) : $(OBJ_A) $(OBJ_C)
	$(CC) $(CFLAGS) -o $@ $^

$(TARGET_3) : $(OBJ_A) $(OBJ_B) $(OBJ_C)
	$(CC) $(CFLAGS) -o $@ $^

clean :
	rm -f $(OBJS) $(TARGET_1) $(TARGET_2) $(TARGET_3)

.PHONY : all clean