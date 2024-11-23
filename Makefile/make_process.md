## Build Process with Makefiles

The C compilation process involves multiple stages that transform source code into an executable:

1. **Preprocessor** (gcc -E)
- Takes .c files as input
- Handles #include directives and macro definitions
- Strips out comments
- Produces preprocessed code

2. **Compiler** (gcc -S)
- Processes preprocessed code
- Translates C code into assembly language
- Creates .S files as output

3. **Assembler** (gcc -c)
- assume it took alreay .s file
- Takes assembly code (.S files)
- Converts assembly into machine code
- Produces object files (.o)

4. **Linker** (gcc -o)
- Combines multiple object files
- Resolves external references
- Creates the final executable
### example
```bash
gcc hello1.o hello2.o -o hello
```

## Makefile Basics for Beginners

**Structure**
```makefile
target: dependencies
    commands
```

**Essential Components**
- **Targets**: Files to be created
- **Dependencies**: Files needed to create the target
- **Commands**: Actions to build the target

**Common Variables**
```makefile
CC = gcc
CFLAGS = -Wall -O2
OBJECTS = main.o helper.o
```

**Basic Rules**
```makefile
all: program

program: $(OBJECTS)
    $(CC) $(OBJECTS) -o program

#purpose: convert .c file to .o file
##which .c? 
%.o: %.c
    $(CC) $(CFLAGS) -c $<	#$< = the first dependency
```

**Important Concepts**
- Use tabs (not spaces) for commands
- Each command runs in a separate shell
- Make only rebuilds what's necessary based on file timestamps
- Use .PHONY for non-file targets like 'clean'

**Common Phony Targets**
```makefile
.PHONY: clean all

clean:
    rm -f *.o program
```
