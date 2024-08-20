# To prevent users from entering invalid (negative) value; to ensure users enter a valid value
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    else:
        print("Pls enter positive value!")

# Create for loop
for _ in range(n): ## _ is "blank variable" ##
    print("meow")

