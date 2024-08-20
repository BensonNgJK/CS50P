# Define function to ask for user input and provide grocery list given EOFError
def main():
    # Create a dict to store inputs
    grocery = {}
    while True:
        try:
            item = input("").upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[f"{item}"] = 1
        except EOFError:
            # Create a list of items sorted alphabetically
            sorted_list = sorted(grocery)
            for key in sorted_list:
                print(grocery.get(key), key)
            break

main()
