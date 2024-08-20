# Ask for inputs (greeting)
greeting = input("Greeting: ")

# Ignore leading whitespaces and lower case
greeting = str(greeting).strip().lower()

# Conditions which translate to payment
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
