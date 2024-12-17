from art import text2art
from replit import clear

logo_m = text2art("Auction", font="slant")

def		get_bid():
	b_list = {}
	def add_bid():
		name = input("Type your name: ")
		b_list[name] = input("Your bidding money: $")
		if not b_list[name].isdigit():
			print("Error: Bidding must be digits")
			return
		next = input("Anyone else near you?[y/n]: ")
		if next == "y":
			clear()
			add_bid()
		else:
			print("Bidding finished\n")
	add_bid()
	return (b_list)

def		print_list(b_list):
	for s, n in b_list.items():
		print(f"name \"{s}\" with a bid amount of \"{n}\"")

def		find_highest(b_list):
	highest = 0
	winner = None
	for s, n in b_list.items():
		if int(b_list[s]) > highest:
			highest = int(b_list[s])
			winner = s
	if winner:
		print(f"the winner is \"{winner}\" with the higest bid \"{highest}\"")
	else:
		print("No bids were placed.")

#start
print(logo_m)
result_list = get_bid()
#print_list(result_list)
find_highest(result_list)