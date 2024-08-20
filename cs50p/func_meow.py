def main():
    number = get_num()
    meow(number)

def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        else:
            print("Pls enter positive value!")

def meow(n):
    for _ in range(n):
        print("meow")

main()
