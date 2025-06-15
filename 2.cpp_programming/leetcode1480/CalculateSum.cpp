#include <stdlib.h>
#include <stdio.h>
#include <iostream> // Add this to use cout

using	namespace std;

#ifdef TEST
void	printIntArray(int arr[], int size)
{
	if (!arr || !size)
		return ; 
	int i = -1;
	cout << "[";
	while(++i < size)
	{
		cout << arr[i];
		if (i < size - 1)
			cout << ",";
	}
	cout << "]\n";
}
#endif

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