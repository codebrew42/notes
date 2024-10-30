#!/bin/bash

#list/arr
files=("text1.txt" "text2.txt")

for file in "${files[@]}"; do
	if [[ -f "$file" ]]; then
		hash=$(sha256sum "$file" | awk '{print $1}')
		echo "SHA-256 hash of $file: $hash"
	else
		echo "$file does not exist"
	fi
done