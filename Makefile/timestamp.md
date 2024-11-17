# time stamps

## definition
- In simple terms, a **timestamp** in Make and Makefiles is a record that shows when a file was last changed. Make uses these timestamps to check if a file that needs to be created (like a program or a part of a program) is current compared to the files it depends on (the files it needs to work).


### How Timestamps Work in Make

1. **Checking Dependencies**: 
   - When you run `make`, it looks at the timestamps of the files it needs to create and compares them to the timestamps of the files they depend on.
   - If any of the dependent files are newer than the file being created, Make will update (rebuild) that file.

2. **Types of Timestamps**:
   - Each file has three important timestamps:
     - **Access Time (atime)**: When the file was last opened.
     - **Modification Time (mtime)**: When the file was last changed.
     - **Change Time (ctime)**: When the file's information or content was last changed.

3. **Rebuilding Files**:
   - If a file doesn’t exist, Make will create it.
   - If a file exists but is older than any of its dependent files, Make will also create it again.


1. **Dependency Tracking**: 
   - When you run `make`, it checks the timestamps of the target files against the timestamps of their dependencies. 
   - If any dependency has a newer timestamp than the target, Make will rebuild the target.

2. **File Types**:
   - Each file typically has three timestamps:
     - **Access Time (atime)**: The last time the file was read.
     - **Modification Time (mtime)**: The last time the file was modified.
     - **Change Time (ctime)**: The last time the file's metadata or content was changed.

3. **Rebuilding Logic**:
   - If a target file does not exist, Make will rebuild it.
   - If a target file exists but its timestamp is older than any of its dependencies, Make will also rebuild it.

## Example

Consider the following Makefile snippet:

```makefile
program: main.o utils.o
    gcc -o program main.o utils.o

main.o: main.c
    gcc -c main.c

utils.o: utils.c
    gcc -c utils.c
```

- When you run `make program`, Make will check the timestamps of `main.o` and `utils.o`.
- If `main.c` is modified and its timestamp is newer than `main.o`, Make will rebuild `main.o`.
- If `main.o` is rebuilt, Make will then check the timestamp of `program` and rebuild it if necessary.

### Timestamp Issues

- **Timestamp Resolution**: Different file systems may have different resolutions for timestamps (e.g., 1-second vs. 1-nanosecond), which can lead to unexpected behavior if not handled properly.
- **Dirty Timestamps**: If files are copied or modified in a way that preserves timestamps incorrectly, it can cause Make to fail to detect changes, leading to stale builds.

## Additional Resources

For more detailed information on timestamps in Make, you can refer to the following resources:
- [GNU Make Manual on Timestamps](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Timestamps-and-Make.html)
- [Wikipedia on Timestamps](https://en.wikipedia.org/wiki/Timestamp)

