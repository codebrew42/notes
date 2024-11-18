# fcntl.h
## meaning
- fcntl stands for *file control*

## purpose
- to control file descriptor

## functions
- `open()`
- `close()`
- `read()`
- `write()`

## constants
- `O_RDONLY`
- `O_WRONLY` : open for write only
- `O_RDWR` : open for read and write
- `O_CREAT` : create the file if it does not exist
- `O_TRUNC` : truncate the file to 0 bytes if it exists


## how to see the man page
- `man fcntl`
- `man 2 open`
- `man 2 close` : here 2 means: system call