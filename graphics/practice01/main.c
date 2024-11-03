#include "mlx_linux/mlx.h"

int main()
{
	void    *mlx_connection;
	void	*mlx_window;
	int	i;

	mlx_connection = mlx_init();
//create window
	mlx_window = mlx_new_window(mlx_connection, 500, 500, "1st_window");

	i = 0;
	while (i++ < 100)
	{
		mlx_pixel_put(mlx_connection, mlx_window, 250+i, 250+i, 0xff0000);
		mlx_pixel_put(mlx_connection, mlx_window, 200+i, 200, 0x43ed35);
		mlx_pixel_put(mlx_connection, mlx_window, 100, 250+i, 0x57ced7);
	}
	//to keep the proc alive
	mlx_loop(mlx_connection);


}
