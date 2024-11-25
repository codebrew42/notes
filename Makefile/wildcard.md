# wildcard
- "*" and "%" are wildcards -->

# *
- can be used in target, prerequisites, or in the wildcard function
- searches filesystem for matching filenames
- **Note:** The `*` wildcard matches any number of characters in a filename.

```bash
var_wrong := *.o #don't! * will not get expanded
# This line will not work as expected because `*` is not expanded in this context.

var_right := $(wildcard *.o)
# This line correctly uses the wildcard function to find all .o files in the current directory.
```

# %
- "matching" mode : it matches one or more chars in string. this match is called the stem
- "replacing" mode : it takes the stem
- **Note:** The `%` wildcard is used in pattern rules to match parts of filenames.

# Pattern Rules

Pattern rules are a powerful feature in Makefiles, but they can be quite confusing for beginners. You can think of them in two ways:

1. **Defining Your Own Implicit Rules**: Pattern rules allow you to create rules that apply to multiple files without having to write a separate rule for each one.
2. **A Simpler Form of Static Pattern Rules**: They provide a more straightforward way to define how to build files based on their names.

## Example 1: Compiling .c Files into .o Files

Here’s a common example of a pattern rule:

```makefile
%.o : %.c
	$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@
```

### Explanation:
- `%.o` is the target pattern. The `%` matches any non-empty string, representing the name of the object file.
- `%.c` is the prerequisite pattern. The `%` here matches the same string as in the target, meaning that for every `.o` file, there is a corresponding `.c` file.
- `$(CC)`, `$(CFLAGS)`, and `$(CPPFLAGS)` are variables that represent the compiler and its flags.
- `$<` is an automatic variable that refers to the first prerequisite (the `.c` file).
- `$@` is another automatic variable that refers to the target (the `.o` file).

## Example 2: Creating Empty .c Files

Here’s another example of a pattern rule that creates empty `.c` files when needed:

```makefile
%.c:
	touch $@
```

### Explanation:
- `%.c` is the target pattern. This rule will match any `.c` file.
- The command `touch $@` creates an empty file with the name of the target. `$@` refers to the name of the target file being created.

## Additional Notes for Beginners:
- **Why Use Pattern Rules?**: They help reduce redundancy in your Makefile. Instead of writing separate rules for each file, you can define a single rule that applies to all files that match the pattern.
- **Automatic Variables**: Familiarize yourself with automatic variables like `$<` and `$@`, as they are essential for writing efficient Makefiles.
- **Testing Your Makefile**: After writing your Makefile, you can test it by running `make` in your terminal. This will execute the rules defined in your Makefile based on the files present in your directory.

By understanding pattern rules, you can create more efficient and maintainable Makefiles for your projects!