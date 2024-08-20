"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).\
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.
"""

# Define main function
def main():
    grocery_list = {}
    create_dict(grocery_list)
    print_list(grocery_list)

# Sort and print the list of grocery
def print_list(list):
    sorted_list = dict(sorted(list.items()))
    for i in sorted_list:
      print(sorted_list[i], i)

# Ask user for inputs and create dictionary
def create_dict(d):
    while True:
      try:
        item = input("").upper()
      except EOFError:
        print("")
        break
      if item not in d:
        d[item] = 1
      else:
        d[item] += 1

# Run program
main()
