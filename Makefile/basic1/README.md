```bash
#can specify the target of "ALL"
jin1@iMac-von-TJ basic1 % make target_abc
gcc -Wall -Wextra -Werror -c  a_code.c -o a_code.o
gcc -Wall -Wextra -Werror -c  b_code.c -o b_code.o
gcc -Wall -Wextra -Werror -c  c_code.c -o c_code.o
gcc -Wall -Wextra -Werror -o target_abc a_code.o b_code.o c_code.o

jin1@iMac-von-TJ basic1 % ./target_abc   
File name : b_code.c
File name : a_code.c
File name : c_code.c
jin1@iMac-von-TJ basic1 % 

```
