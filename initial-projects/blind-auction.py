ask = "yes"
bid = {}
highest = []
while ask == "yes":
    name = input("Enter your name: ")
    money = int(input("How much you want to bid: "))
    highest.append(money)
    bid[name] = money
    ask = input("Do you want to continue? type 'yes' or 'no' : ")
    clear()
    if ask == "no":
        high_amt = max(highest)
        new_bid={}
        for name, money in bid.items():
            new_bid[money] = name
        print(f"the highest bidder is {new_bid[high_amt]} with the amount of {high_amt}")
