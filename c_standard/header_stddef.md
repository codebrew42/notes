# functions

## size_t
- used for sizes and counts
- always unsigned
```c
size_t large = SIZE_MAX;

size_t len = strlen(s);
void *malloc(size_t size);
size_t arr_size = sizeof(array);

printf("%zu", len);
```

## NULL
```c
#define NULL ((void *) 0)

int *ptr = NULL;
if (ptr = NULL)
{

}
```