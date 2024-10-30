ls -R > output.txt

grep -r "text_to_find" directory

grep -r "text" .
-> cur and sub, all files


grep -ri "text" dir
-> regardless of capital letter, small letter,

grep -rn "text" dir
-> show the results name, line 

grep -r --include="*.txt" "검색어" 디렉토리명
-> search only .txt

grep -r --include="*.log" "error" .