#include <stdio.h>

void	count_func_call_1(void)
{
	int	count = 0;
	printf("func call (%d)\n", count++);
}

void	count_func_call_2(void)
{
	static int	count = 0;
	printf("func call (%d)\n", count++);
}

int	main(void)
{
	printf("function count: using local var \n");
		count_func_call_1();
	count_func_call_1();
	printf("function count: using static var \n");
	count_func_call_2();
	count_func_call_2();
	return (0);
}