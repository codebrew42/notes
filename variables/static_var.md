# static var

## what is it?
- static variable: 
	- definition: a variable that is allocated storage in the static storage duration
		
	- scope: the block in which the variable is defined, or the file in which the variable is defined (if it is a global variable)
	- lifetime: the entire execution of the program


## how to use?
### the most common example : c program
@[example](../cmp1_static_vs_local/static_vs_local.c)

why this difference occurs?
- static variable retains its value between function calls
	- how is it possible? 
		- because the static variable is allocated storage in *the static storage duration*, and it retains its value between function calls
- local variable does not retain its value between function calls
	- because the local variable is allocated storage in the *automatic storage duration*, and it does not retain its value between function calls