# nested list

## code
```python
arr = ["a", "b", "c", ["d", "e", "f"]]

print(arr[3][2])
```

## output
```
f
```

# nested list in dict

## code
```python
travel_log = {
	"Korea": {
		"cities visited": {
		"Seoul", "Busan", "Pohang"
	},
		"visit times": {
			100, 20, 5
		}
	},
	"Germany": {
		"Stadt": {
			"Berlin", "Muenchen"
		},
		"Besuchen": {
			1, 5
		}
	}	
}
```
## characteristics
### case: Must convert dict to a list
- In Python, *sets* of dicts are *unordered collections* of unique elements, meaning you cannot access their elements by index. To access specific elements by index, you must convert the set to a list, which is ordered. 
- This allows you to use indexing to retrieve elements. If you want to access elements from a set without converting it, you can iterate through the set, but you won't be able to access them by index.
- code
```python

#to print 5 of "Besuchen" : convert dict to a list
print("1st option: \t")
print(list(travel_log3["Germany"]["Besuchen"])[1])

print("2nd option: \t")
for value in travel_log3["Germany"]["Besuchen"]:
    print(value) 
```