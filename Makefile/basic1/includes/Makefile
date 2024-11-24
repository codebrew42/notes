#compile : target_abc
TARGET_3		:= target_abc

CC				:= gcc
CFLAGS			:= -Wall -Werror -Wextra

SRC_DIR			:= ..
SRCS			:= $(SRC_DIR)/a_code.c	$(SRC_DIR)/b_code.c	$(SRC_DIR)/c_code.c

#create this dir, if it doesnt exist
OBJ_DIR			:= ../obj
OBJS			:= $(OBJ_DIR)/a_code.o	$(OBJ_DIR)/b_code.o	$(OBJ_DIR)/c_code.o

all: $(OBJS) $(TARGET_3)

#OBJS depends on OBJ_DIR, so it will creates if there is no any.
$(OBJS): | $(OBJ_DIR)

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

$(OBJ_DIR)/%.o : $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

target_abc : $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

clean : $(OBJS)
	rm -f $(OBJS) $(TARGET_3)

.PHONY : all clean