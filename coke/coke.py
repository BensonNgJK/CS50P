# Define main function
def main():
    due = 50
    payment(due)

def payment(due):
    while True:
        # Print amount due and ask for coin payment
        if due > 0:
            print(f"Amount Due: {due}")
            payment = int(input("Insert Coin: "))
            # To ensure valid payment
            if payment == 25 or payment == 10 or payment == 5:
                due -= payment
        # Print change owed when amount due is equal or less than zero
        else:
            print(f"Change Owed: {-due}")
            break

main()
