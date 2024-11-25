# example
```bash
code: code.o
	cc code.o -o code1

code.o : code.c
	cc -c code.c -o code.o

code.c:
	echo "int main() { return 0; }" > code.c
```
## flow
- code.c -> code.o -> code