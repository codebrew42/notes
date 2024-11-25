# definition
- Makefile is a build system
- C/C++ also has alternative build system : Scons, CMake, Bazel, and Ninja
- Interpreted languages(Python, Ruby, JS...) don't require an analoague to Makefiles
	- why? when the prog runs, the most recent ver of the file is used.

# purpose
## 1. help compilation
- help compilation based on what files have been changed.
- mostly C or C++ files, other languages have their own tools like Make
	- Java has *Ant*, *Maven*, and *Gradle*

## 2. serious of instruction
- run serious of instruction depending on *what files* have changed

# default setting: basic fact
## target
- the first target is the *default target*

## basic structure
- targets: prerequisites
	command

# *prerequisites*
- only when having prerequisites, Make run target *code1*, only when code1.c is newer than code1
```bash
code1:
	cc code1.c -o code1
```
- try make -> modify code1.c -> make
- nothing happens, even after modifying code1.c

```bash
code1: code1.c
	cc code1.c -o code1
```
- make -> modify code1.c -> make 
: make recompiles the file

# Understanding the Make Process

When you run `make`, the following sequence of steps occurs:

1. **Default Target Selection**: The first target in the Makefile is selected as the default target. This is the target that will be executed unless specified otherwise.

2. **Prerequisite Check**: The selected target has associated prerequisites (e.g., `blah.c`). Make checks whether it should execute the target based on the status of its prerequisites.

3. **Decision to Run**: Make will only run the target if:
   - The target file (e.g., `blah`) does not exist, or
   - The prerequisite file (e.g., `blah.c`) is newer than the target file.

4. **Essence of Make**: This step is crucial as it determines whether the prerequisites have changed since the last compilation of the target. If `blah.c` has been modified, running `make` will trigger a recompilation of the target. Conversely, if `blah.c` has not changed, the target will not be recompiled.

5. **File System Timestamps**: Make uses file system timestamps as a heuristic to determine if a file has changed. Typically, a file's timestamp will only update when the file is modified. However, it's important to note that timestamps can be manipulated. For instance, if you modify a file and then set its timestamp to an earlier time, Make may incorrectly assume that the file hasn't changed and skip recompilation.

### heuristic
- practical approach to problem-solving that is not guaranteed to be perfect, but sufficient for reaching the goal
- in the case of Makefile, the heuristic refers to the method of determining whether a file has changed, based on the fact wheather the timestamp is newer than that of its target.



## source
[tutorial](https://makefiletutorial.com/#why-do-makefiles-exist)