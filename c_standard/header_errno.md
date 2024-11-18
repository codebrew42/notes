# errno.h

## meaning
- errno stands for *error number*
- errno.h defines a macro named `errno`

## purpose
- allows to diagnose issues and respond to them
- to store the error number
- after callung functions like file operation(open, read, write, close, etc.), memory allocation(malloc, free, etc.	), socket operation(socket, bind, listen, accept, etc.), the error number is set by the system

## functions
- `perror()` : print the error message
- `strerror()` : convert errno to human-readable string

## how to see the man page
- `man 3 perror`
- `man 3 strerror`

## example
```c
#include <stdio.h>
#include <errno.h>
#include <string.h>

void example_function() {
    FILE *file = fopen("non_existent_file.txt", "r");
    if (file == NULL) {
        // An error occurred, check errno
        printf("Error opening file: %s\n", strerror(errno));
    }
}
```

## Error code
- ENOENT : No such file or directory
- EACCES : Permission denied
- EINTR : Interrupted system call
- EIO : I/O error
- EAGAIN : Try again
- EFAULT : Bad address
- EINVAL : Invalid argument
- E2BIG : Argument list too long
- ENOEXEC : Exec format error
- ENOMEM : Not enough memory
- ELOOP : Too many symbolic links encountered

