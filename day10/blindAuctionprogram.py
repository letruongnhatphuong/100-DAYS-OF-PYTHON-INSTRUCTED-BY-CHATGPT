import art

def get_bid():
    """Helper function to collect one bidder's name and bid."""
    while True:
        name = input("What is your name?: ").strip().title()
        if not name or name.isdigit():
            print("❌ Invalid name. Please enter a valid name (letters only).")
            continue
        try:
            bid = int(input("What is your bid?: $"))
            if bid <= 0:
                print("❌ Bid must be greater than 0.")
                continue
            return name, bid
        except ValueError:
            print("❌ Please enter a valid number for your bid.")

def find_highest_bidder(bidding_record):
    """Return the highest bidder and amount."""
    winner = max(bidding_record, key=bidding_record.get)
    amount = bidding_record[winner]
    return winner, amount

def blind_auction():
    print(art.logo)
    print("Welcome to the secret auction program.\n")

    bids = {}
    while True:
        name, bid = get_bid()
        bids[name] = bid

        more = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more != "yes":
            break

    winner, amount = find_highest_bidder(bids)
    print(f"\n🏆 The winner is {winner} with a bid of ${amount}!")

if __name__ == "__main__":
    blind_auction()