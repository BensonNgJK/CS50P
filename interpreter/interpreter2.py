# Ask for user inputs
expression = input("Expression: ")

# Break down the string into sequence of value
num_1, arith, num_2 = expression.split(" ")

# Calculate the following
if arith == "+":
    print(float(num_1) + float(num_2))
elif arith == "-":
    print(float(num_1) - float(num_2))
elif arith == "*":
    print(float(num_1) * float(num_2))
elif arith == "/":
    print(float(num_1) / float(num_2))
else:
    print("Error: Function is undefined!")
