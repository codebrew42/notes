# grep (Global Regular Expression Print)
## definition
- grep is a command-line utility used to search for patterns in each file.

## how it works
- grep reads through a file line by line, searching for a pattern.
- when the pattern is found, grep prints the line to the screen.

## basic usage
```bash
#grep <pattern> <file/files>
grep text file.txt
grep text *.txt 
#case-insensitive search
grep -i <pattern> <file>
#recursive search
grep -i <pattern> <file>
# regular expression
grep -E <pattern> <file>
grep -E "pico.*CTF" file.txt

```
## match whole word
```bash
#grep -w <pattern> <file>
grep -w pico file.txt
```
- mathces "pico" as a whole word, not like "picot"

- if "file" contains pico.*CTF
## display line numbers
```bash
grep -n <pattern> <file>
```

## display : count matches
```bash
grep -c <pattern> <file>
```

## invert match
```bash
grep -v <pattern> <file>
```
- display lines that do not match the pattern