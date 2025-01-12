# Guide to sed

## What is sed?
`sed` (stream editor) is a Unix utility that parses and transforms text from a data stream or file. It is commonly used for text substitution, deletion, and insertion.

## Basic Syntax
```
sed [options] 'command' file
```

## Common Commands
1. **Substitution**: Replace occurrences of a string.
   ```
   sed 's/old_string/new_string/' filename
   ```

2. **Delete Lines**: Remove lines matching a pattern.
   ```
   sed '/pattern/d' filename
   ```

3. **Print Lines**: Print specific lines.
   ```
   sed -n '2,5p' filename  # Print lines 2 to 5
   ```

4. **In-place Editing**: Edit a file directly.
   ```
   sed -i 's/old_string/new_string/g' filename
   ```

## Example: Deleting Lines Starting with an Alphabet
To delete lines starting with any alphabetic character and create a backup of the original file:
```
sed -i '.bak' '/^[a-zA-Z]/d' ./obj/res1
```
- `-i '.bak'`: Edits the file in place and creates a backup with the `.bak` suffix.
- `'/^[a-zA-Z]/d'`: Matches lines starting with any letter and deletes them.

## Conclusion
`sed` is a powerful tool for text processing in Unix/Linux environments. It can be used for a variety of tasks, including text substitution, deletion, and more.

