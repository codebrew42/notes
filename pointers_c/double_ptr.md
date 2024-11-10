# Double Pointer NULL Termination: Two Important Cases

## Case 1: String NULL Termination ('\0')
```c
str[i] = "Hello\0"    // Each individual string ends with '\0'
```
- Terminates each individual string
- Tells string functions where each string ends
- Added automatically by string functions like strdup, strcpy
- Used by: strlen(), strcpy(), etc.

## Case 2: Pointer Array NULL Termination (NULL)
```c
char **array = [
    ptr1 -> "Hello\0",
    ptr2 -> "World\0",
    ptr3 -> "!\0",
    NULL             // End of pointer array
]
```
- Terminates the array of pointers
- Tells array functions where the list of pointers ends
- Must be manually added: array[last_index] = NULL
- Used by: while(array[i]) loops

## Memory Allocation Comparison
### Without Pointer Array NULL Termination
```c
char **array = malloc(sizeof(char *) * row_count);
// Must use counter: while (i < row_count)
// Reading array[row_count] is undefined behavior!
```

### With Pointer Array NULL Termination
```c
char **array = malloc(sizeof(char *) * (row_count + 1));
array[row_count] = NULL;
// Can use: while (array[i] != NULL)
// Safe to read array[row_count], will find NULL
```

## Remember!
- String NULL ('\0') is for string content
- Pointer NULL is for array of pointers
- Using while(array[i]) without NULL termination is like reading past the end of a book!

## Memory Visualization
```
Memory Layout Without NULL Termination (Dangerous!):
[Allocated Memory for array]
Address:    Content:
0x100 ->    ptr1 ("Hello\0")
0x108 ->    ptr2 ("World\0")
0x110 ->    ptr3 ("!\0")
0x118 ->    ??? (Unknown/Invalid memory)  <-- Problem happens here!

Memory Layout With NULL Termination (Safe):
[Allocated Memory for array]
Address:    Content:
0x100 ->    ptr1 ("Hello\0")
0x108 ->    ptr2 ("World\0")
0x110 ->    ptr3 ("!\0")
0x118 ->    NULL   <-- Safe termination point
```
```