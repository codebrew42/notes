## if you want to use runtime variable as a value

- Pros of Using Vectors 
- it can be used with Runtime Variables in C++98
- `std::vector` is designed specifically to handle dynamically sized collections whose size is determined at runtime. This is one of the key differences between arrays and vectors in C++.

### example1: invalid
```cpp

int main(int ac, char *av[])
{
	if (ac < 2)
	{
		fprintf(stderr, "Error: Numbers must be given!(e.g., 3,1,2)");
		exit(EXIT_FAILURE);
	}
//1. convert INPUT to int array
//c++98: doesn't support var-length wehre that is runtime value
//so use vector instead
	int arrSize = ac - 1;
	int arr[arrSize];
	int i = -1;
	while (++i < arrSize)
	{
		arr[i] = atoi(av[i+1]); //how to convert char* to int: atoi()
	}
#ifdef TEST
	printIntArray(arr, arrSize);

#endif
	return 0;
}

```
### example2: valid
```cpp


int main(int ac, char *av[])
{
    if (ac < 2)
    {
        fprintf(stderr, "Error: Numbers must be given!(e.g., 3,1,2)\n");
        exit(EXIT_FAILURE);
    }
    
    // Convert INPUT to int vector
    int arrSize = ac - 1;
    vector<int> arr(arrSize); // Use vector instead of C99 VLA
    int i = -1;
    while (++i < arrSize)
    {
        arr[i] = atoi(av[i+1]);
    }
    
#ifdef TEST
    printIntArray(arr);
#endif

    return 0; // Explicit return statement
}
```