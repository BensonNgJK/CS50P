# define main function
def main():
    x, y , z = input("Expression: ").split(" ")
    x = int(x)
    z = int(z)
    calculate(x, y, z)

# Define function to calculate
def calculate(x , y, z):
    if y == "+":
        ans = x + z
        print(f"{ans:.1f}")
    elif y == "-":
        ans = x - z
        print(f"{ans:.1f}")
    elif y == "*":
        ans = x * z
        print(f"{ans:.1f}")
    elif y == "/":
        ans = x / z
        print(f"{ans:.1f}")

main()
