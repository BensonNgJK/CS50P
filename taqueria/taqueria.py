# Dictionary of various items on Falipe's Menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Define main function
def main():
    total("Item: ")

# Define function which prompt user for input and return total
def total(prompt):
    total = 0
    while True:
        try:
            item = input(prompt).title()
            if item in menu:
                total += menu.get(item)
                print(f"Total: ${total:.2f}")
        except EOFError:
            print("", end="\n")
            break

main()
