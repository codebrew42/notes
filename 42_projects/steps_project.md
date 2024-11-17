#

# steps to start a project

1. read the subject, summarize it in the note (directory: subject)

2. plan and note down the steps (directory: coding_plan)

3. write header file (directory: code/include/<project_name>.h)

4. write main function (directory: code/main.c)

5. write test code (directory: test) and so on...
(!) Do not look at the reference code for 2-3 days

6. find where I get stuck -> note it down & discuss with others/claude(dont ask about the answer, ask about the way to solve it)

7. don't make a variation code of the reference code. make your own code.

# steps to finish

1. check norminette (for all subdirectories: norminette -R CheckForbiddenSourceHeader)
2. check Makefile (follow norminette rules)
3. ls -R (check all files which should be submitted)
