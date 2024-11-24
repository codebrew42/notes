# go to the prev commit
```c
git checkout HEAD^
```

# go to the specific commit
```c
git checkout <commit-id>
git checkout HEAD~N # go to the Nth commit: HEAD~1 is the previous commit, HEAD~2 is the commit before the previous commit...
```

## what is commit-id?

commit-id is the id of the commit, you can get it by `git log`