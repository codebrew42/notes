travel_log = {
	"France": ["Paris", "Oleron"],
	"Korea": ["Busan", "Pohang", "Seoul"]
}

print(travel_log)

#print one element
print("dict[\"France\"][1]", travel_log["France"][1])

#basic nested list
nested = ["a", "b", "c", ["d", "e", "f"]]
print("nested[2]", nested[2])
print("nested[2][0]", nested[2][0])
#print("nested[2][1]", nested[2][1]) #wrong
print("nested[3][1]", nested[3][1])

#advanced nested list in dict
travel_log2 = {
	"France": {
		"cities_visited": ["Paris", "Oleron"],
		"total_visits": 12
	},
	"Korea": {
		"cities_visited": ["Busan", "Pohang", "Seoul"],
		"total_visits": 100
	}
}

print("travel_log2[\"France\"]", travel_log2["France"])

print("\nPRACTICE 3")

travel_log3 = {
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

print(travel_log3["Germany"])
print(travel_log3["Germany"]["Besuchen"])

#to print 5 of "Besuchen" : convert dict to a list
print("2nd option: \t")
print(list(travel_log3["Germany"]["Besuchen"])[1])

print("2nd option: \t")
for key in travel_log2:
    print(key)
for value in travel_log3["Germany"]["Besuchen"]:
    print(value) 