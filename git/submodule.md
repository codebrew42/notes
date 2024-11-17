# submodule

## steps

1. git submodule add <repo_url> <path>
2. git commit -m "add submodule"
3. git push
4. when I open that repo, it will be empty. so I need to clone it.
5. git submodule update --init --recursive
-> this enables me to get the submodule's code.

