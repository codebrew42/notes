# challenge
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 

Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3

love score = 53

# solution 1 : use arr

```python
def cal(name1, name2):
	arr_true = "TRUE"
	arr_love = "LOVE"
	count_true = 0
	count_love = 0
	combined_names = (name1 + name2).upper()

	for char in combined_names:
		if char in arr_true:
			count_true += 1
		if char in arr_love:
			count_love += 1

	total = str(count_true) + str(count_love)
	return (total)
```