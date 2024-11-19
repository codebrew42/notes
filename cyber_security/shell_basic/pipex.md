# how to use pipex

## how to search for a string in a file
```bash
cat file.txt | grep "hello"
```

## how to search for a string in a subdirectory
```bash
find . -type f -name "*.txt" | xargs grep "hello"
```

### xargs

xargs is a command that takes the output of a command and passes it as arguments to another command.
