import random

def coin_flip():
    print("\n'IT' holds up a Golden coin.")
    while True:
        choice = input("Choose a side -- heads or tails -- : ").lower().strip()
        if choice in ("heads", "tails"):
            break
        print("Choose heads or tails.")

    print("The coin spins through the air...")
    result = random.choice(["heads", "tails"])
    print(f"It lands on {result}.")
    return choice == result