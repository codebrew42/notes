# closing the disp

- mlx_destroy_display

# doc
https://harm-smits.github.io/42docs/libs/minilibx

# minilibx
## def
- tiny graphics lib which allows u to do basic things for rendering sth in screen without knowlege of X-window and Cocoa
- provides simple window creation, drawing tool, image functions, event management system

# x-window
## def
- network-oriented graphical system for unix
- common example : teamviewer

# mac OS
- to access the graphical access to its screen, we must register our app to the underlying macOS graphical framework

# minilibx_functions
## 1. mlx_init
### what it does
- t_xvar : malloc & check
- XOpenDisplay("") : open, free if fails
- assgin val to...
	t_xvar->screen/root/cmap/deapth/win_list/loop_hoop/loop_param/do_flush_wm_delete_window/wm_
- return val : can be saved to "void *mlx_connection"

### 1-1. XOpenDisplay()
### def
- provides a low-level C prog interface to interact with the X window system
- returns display
- to open a connection btw a client application and the X server
-> allows the app to create windows, draw graphics, manage event(mous clicks, key presses)
### how it works
- connection attempt
	try to connect to an X server specified by an env var called "DISPLAY"
	env var: contains adr of the display (hostname:dispnbr.screennbr)
	z.B localhost:0.0 (first screen on the local host)
- return value
	if suc, returns a pointer to a Display structure
- err handling
	if fails, returns NULL
	indicates issue with the DISPLAY env var

## 2. mlx_new_window(t_xvar *xvar, int size_x, int size_y, char *title)
- title : title of the window?
- return val : saved to "void *window1", "void *window2"...

- example
	void *window1;

	window1 = mlx_new_window(); mlx_ptr: size_x: size_y: title:
	if (NULL = window1)
		mlx_destroy_display(mlx_connection); mlx_ptr;
		free(mlx_connection); ptr;
		return (MALLOC_ERROR);
	


## 3. mlx_loop(mlx_connection)
### def
- keeps the prog alive
- thanks to the loop, can see the window
- can have multiple windows

## 4. mlx_destroy_window()
### char
- can have multiple windows

## 5. mlx_destroy_display()

## 6. free()