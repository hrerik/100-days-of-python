bidders = {}

playing = True
while playing:
    print("############################# BLIND AUCTION #############################")
    bidder = input("What's the name of the bidder?\n")
    amount = int(input("How much will this bidder pay?\n$"))
    bidders[bidder] = amount

    while True:
        inp = input("Are there more bidders? (yes/no)\n")
        if inp == "yes":
            break
        elif inp == "no":
            playing = False
            break
        print("Invalid response")

    print("\n"*100) # "clear screen"

highest_bidder = "[ERROR]" # error just for fun (if no one paid more than 0 than cancel the auction)
highest_amount = 0
for bidder in bidders:
    amount = bidders[bidder]
    if amount > highest_amount:
        highest_bidder = bidder
        highest_amount = amount

print(f"Congratulations!! {highest_bidder} had the highest bid, paying ${highest_amount}.")
print(bidders)