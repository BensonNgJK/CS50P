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

## print(list(menu.values()))

"""
i = "Taco"
print(menu[i])
if i in menu:
    menu[i] += 1
print(menu[i])

a = "beans"
if a not in menu:
    menu[a] = 1

print(list(menu.keys()))

for food in menu:
    print(food.upper(), menu[food])
"""

# define main function which create a dictionary
def main():
    grocery_list = {}
    while True:
      try:
        item = input("").upper()
      except EOFError:
        print("")
        break
      if item not in grocery_list:
        grocery_list[item] = 1
      else:
        grocery_list[item] += 1

    sorted_list = dict(sorted(grocery_list.items()))
    for i in sorted_list:
      print(sorted_list[i], i)

main()
