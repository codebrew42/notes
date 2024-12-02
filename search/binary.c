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
	count = 0;
	while (left <= right)
	{
		mid = left + (right - left) / 2; //int
		if (target == arr[mid])
		{
			printf("(count: %d) target '%d' found", count, target);
			return (0);
		}
		else if (target < arr[mid])
			left = mid + 1;
		else
			right = mid - 1;
		count++;
	}
	return (-1);
}

int	*bubble_sort(int arr[], int size)
{
	int	i;
	int	j;
	int	temp;
	int	*res;

	res = arr;
	i = 0;
	while(i < size - 1)
	{
		j = 0;
		while(j < size - i - 1)
		{
			if (res[j] > res[j+1])
			{
				temp = res[j];
				res[j] = res[j+1];
				res[j+1] = temp;
			}
			j++;
		}
		i++;
	}
	return (res);
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
	bubble_sort(arr, 20);
	print_arr(arr);
	binary_search(arr, 20, arr[5]);
	return (0);
}