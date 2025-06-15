# Fun fact about malloc
## where you malloc matters

```c
int	main(int ac, char **av)
{
	t_arg	*arg;

	if (ac != 5)
		exit_on_error("Number of arguments should be 5");
	arg = malloc(sizeof(t_arg));
	if (!arg)
		exit_on_error("Malloc failed");
	get_args(arg, av);
	check_functions(arg);
}
```

- if you malloc inside the functions like "get_args" here,  
it will cause seg fault. to avoid this, read this note

# note

The behavior of `malloc` and the potential for segmentation faults depend on how memory is allocated and accessed in your program. Let's break down the scenarios to understand why allocating memory inside `get_args` could lead to a segmentation fault, while allocating memory in `main` works correctly.

### Scenario 1: Allocating Memory in `main`

In your provided code snippet, you allocate memory for `arg` in `main`:

```c
arg = malloc(sizeof(t_arg));
if (!arg)
    return(1);
```

- **Memory Allocation**: Here, you allocate memory for a single `t_arg` structure and check if the allocation was successful.
- **Pointer Validity**: The pointer `arg` now points to a valid memory location that you can safely use in subsequent function calls like `get_args(arg, av);` and `check_functions(arg);`.

### Scenario 2: Allocating Memory Inside `get_args`

If you were to allocate memory inside the `get_args` function like this:

```c
void get_args(t_arg *arg, char **s)
{
    arg = malloc(sizeof(t_arg)); // This allocates memory but does not affect the pointer in main
    if (!arg)
        exit_on_error("Memory allocation failed");
    // ... populate arg ...
}
```

- **Local Pointer**: In this case, `arg` is a local variable in `get_args`. When you do `arg = malloc(sizeof(t_arg));`, you are allocating memory and assigning it to the local `arg` pointer, which does not affect the `arg` pointer in `main`.
- **Lost Reference**: After the function `get_args` returns, the local `arg` pointer goes out of scope, and the memory you allocated is not accessible anymore. The original `arg` pointer in `main` remains `NULL` (or whatever it was before), leading to potential segmentation faults when you try to access it later.

### Key Differences

1. **Scope of Pointer**:
   - In `main`, `arg` is a pointer that is allocated memory and remains valid throughout the lifetime of `main`.
   - In `get_args`, if you allocate memory to a local pointer, it does not affect the pointer in `main`, leading to a loss of reference to the allocated memory.

2. **Accessing Memory**:
   - After allocating memory in `main`, you can safely access and manipulate the memory pointed to by `arg`.
   - If you allocate memory in `get_args` without returning the pointer or modifying the original pointer, you will end up with a dangling pointer or a pointer that points to an invalid location, causing segmentation faults when accessed.

### Correct Approach for Allocating Inside Functions

If you want to allocate memory inside `get_args` and have it accessible in `main`, you can either:

1. **Pass a Pointer to Pointer**:
   ```c
   void get_args(t_arg **arg, char **s)
   {
       *arg = malloc(sizeof(t_arg)); // Allocate memory and assign it to the original pointer
       if (!*arg)
           exit_on_error("Memory allocation failed");
       // ... populate *arg ...
   }
   ```

   Then call it in `main` like this:
   ```c
   get_args(&arg, av); // Pass the address of arg
   ```

2. **Return the Pointer**:
   ```c
   t_arg *get_args(char **s)
   {
       t_arg *arg = malloc(sizeof(t_arg)); // Allocate memory
       if (!arg)
           exit_on_error("Memory allocation failed");
       // ... populate arg ...
       return arg; // Return the pointer
   }
   ```

   Then call it in `main` like this:
   ```c
   arg = get_args(av); // Assign the returned pointer
   ```

### Conclusion

The key takeaway is that the scope and lifetime of pointers matter significantly when using `malloc`. Always ensure that the pointer you are working with remains valid and accessible throughout the necessary scope to avoid segmentation faults.
