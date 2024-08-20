def main():
    amount_due = int(50) # Cost of a bottle of Coke
    while True:
        print("Amount Due:", amount_due)
        amount_due -= payment(insert_coin())
        if amount_due <= 0:
            break
    change(amount_due)

# function which print change owed
def change(c):
    return print("Change Owed:", abs(c))

# ask user for inputs
def insert_coin():
    return int(input("Insert Coin: "))

# test if coin payment is successful or otherwise
def payment(i):
    match i:
        case int(25) | int(10) | int(5):
            return int(i)
        case _:
            return int(0)

# Run program
main()
