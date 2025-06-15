NAME = calculator
CC = c++
CFLAG = -Wall -Wextra -Werror -std=c++98
SRC = CalculateSum.cpp
OBJ = $(SRC:.cpp=.o)
#TEST = CFLAG += -DTEST

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAG) $(OBJ) -o $@

%.o: %.cpp
	$(CC) $(CFLAG) -c $< -o $@

clean:
	rm -rf $(OBJ)

fclean: clean 
	rm -rf $(NAME) 

re: fclean all

.PHONY: all fclean clean re