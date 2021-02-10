from art import logo
from clear_stuff import clear

print(logo)
print("Welcome to the Auction how much will you bid for my gavel?")

other_bidders = True
bidders = {}

while(other_bidders):
    clear()
    print(logo)
    print("Welcome to the Auction how much will you bid for my gavel?")

    name = input("What's your name? > ")
    bid_price = float(input("How much is your price? > "))

    bidders[name] = bid_price

    choice = input("Any more bidders? yes or no > ").lower()
    if choice != "yes":
        break

winner = max(bidders, key=bidders.get)
print(f'{winner} won the gavel !! priced at ${bidders[winner]} ')