# example 00
computed=$(sha256sum "$file" | awk '{print $1}')

## sha256sum

command-line util that
	(1)reads contents of file
	(2)outputs SHA-256 checksum along with the filename


# example 01
       if [ $# -eq 0 ]; then
            echo "blah blah"
            exit 1
		if [ $# -ne 1 ]; then
    		echo "plah plah"
    		exit 1
        fi

## argv
- $# : nbr of parameters/arguments 

## exit
- terminate the script immediately

- exit 0 : suc
- exit 1 : general err
- exit 2 : misuse of shell built-ins / don't fit general err 

## fi
- mark the end of 'if'


# comparison operators
### Numeric Comparison Operators
- eq: Equal
- ne: Not equal
- lt: Less than
- le: Less than or equal to
- gt: Greater than
- ge: Greater than or equal to

### String Comparison Operators
- =: Equal
- !=: Not equal
- <: Less than (for lexicographic comparison)
- \>: Greater than (for lexicographic comparison)
- -z: String is null (empty)
- -n: String is not null (not empty)

# example 02
	files=("file1.txt" "file2.txt")

	for file in "${files[@]}"; do
		echo "Processing $file"
	done

## (bash) array
	files=("file1.txt" "file2.txt" "file3.txt")

	echo "${files[0]}"  # Outputs: file1.txt

	echo "${#files[@]}"  # number of elm: 3

- store multiple elem(str/nb/any other data type) in a single var
- idx: starting from 0

## for - done
## if - fi

## loop through the arr
	for file in "${files[@]}"; do
  	  echo "Processing $file"
	done
