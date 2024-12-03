#include <stdlib.h>
#include <stdio.h>

int	binary_search(int *arr, int size, int target)
{
	int	left;
	int	right;
	int	mid;
	int	count;

	left = 0;
	right = size - 1;
	count = 1;
	while (left <= right)
	{
		mid = left + (right - left) / 2; //int
		if (target == arr[mid])
		{
			printf("\n(count: %d) target '%d' found", count, target);
			return (0);
		}
		else if (target > arr[mid])
			left = mid + 1;
		else
			right = mid - 1;
		printf("\n(count: %d) target '%d' not found", count, target);
		count++;
	}
	return (-1);
}
//	idx	 : 0 1 2 3 4
//size 5 : a b c d e
void	bubble_sort(int arr[], int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < size - 1)
	{
		j = 0;
		while (j < size - 1 - i)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
			j++;
		}
		i++;
	}
}

void	print_arr(int *arr)
{
	int	j;

	j = 0;
	while (j < 20)
	{
		printf("(%d)%d ", j, arr[j]);
		j++;
	}
}
/**
 * @brief create an random int arr, do binary search
 */
int	main()
{
	//create an array containing 20 random arr
	int	arr[20];
	int	j;
	for (int i = 0; i < 20; i++)
	{
		arr[i] = rand() % 100;
	}
	// bubble sort
	printf("before buble sort: \n");
	print_arr(arr);
	bubble_sort(arr, 20);
	printf("\n\nafter buble sort: \n");
	print_arr(arr);
	binary_search(arr, 20, arr[0]);
	return (0);
}