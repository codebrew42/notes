# 241217
## what I learned : Python
- when comparing value which is given on the terminal, convert it into int
```python
b_list = {}

def get_info():
	b_list = {}
	def collect():
		name = input("your name: ")
		bid = input("your bid: $")
		b_list[name] = bid
		next = input("next person[y/n]: ")
			if next == "y":
				collect()
			else:
				print("bid finished")
	collect()
	return b_list

def find_highest_bid(b_list):
	highest = 0
	winner = None
	for name, bid in b_list.items():
		if int(bid) > higest:
			...
```

- without int, it cannot compare, it remains as string.

# 250112

## what I learned : command
```bash
# to save the output of the command
./obj/philo 5 800 200 200 10 > ./obj/res1


#[1]to remove the line which starts with any alphabet

# mac : 
sed -i '' '/^[a-zA-Z]/d' ./obj/res1
sed -i '.bak' '/^[a-zA-Z]/d' ./obj/res1 # to save the original file : *.bak

# linux : 
sed -i '/^[a-zA-Z]/d' ./obj/res1
sed -i '.bak' '/^[a-zA-Z]/d' ./obj/res1 # to save the original file : *.bak

# [2] using grep
grep -v '^[0-9]' ./obj/res1 > ./obj/res1_filtered

```
