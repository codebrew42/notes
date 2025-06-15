from art import text2art

logo_m = text2art("Auction", font="slant")



def get_bid():
	bids = {}
	def collect():
		name = input("your name: ")
		bids[name] = input("your bidding money: $")
		next = input("any other person near you?: [yes/no]")
		if next == "y":
			collect()
	collect()
	return bids

def find_winner(bids):
	highest = 0
	winner = ""
	for name, bid in bids.items():
		bid = float(bid)
		if bid > highest:
			highest = bid
			winner = name
	print(f"The winner is \"{winner}\" with a bid of ${highest}")

print(logo_m)
bids = get_bid()
find_winner(bids)