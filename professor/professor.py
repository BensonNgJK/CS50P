# Import revalent libraries/functions
from random import randint

# Define main function
def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        response = input(f"{x} + {y} = ")
        tries = 1
        while True:
            try:
                if int(response) == ans:
                    score += 1
                    break
                elif int(response) != ans:
                    raise ValueError
            except ValueError:
                if tries < 3:
                    print("EEE")
                    tries += 1
                    response = input(f"{x} + {y} = ")
                    pass
                else:
                    print(f"{x} + {y} = {ans}")
                    break
    print(f"Score: {score}")

# Ask user for input (level 1 to 3)
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)

if __name__ == "__main__":
    main()
