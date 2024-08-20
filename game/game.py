# Import revalent libraries/functions
from random import randint


# Define main function
def main():
    ans = level("Level: ")
    guess("Guess: ", ans)


# Function to prompt user for level and return random integer
def level(prompt):
    while True:
        try:
            lvl = int(input(prompt))
            if 1 <= lvl <= 100:
                return randint(1, lvl)
            else:
                pass
        except ValueError:
            pass


# Function to prompt user for guess until correct answer
def guess(prompt, n):
    while True:
        try:
            guess = int(input(prompt))
            ans = n
            if guess == ans:
                print("Just right!")
                break
            elif guess > ans:
                print("Too large!")
                pass
            elif guess < ans:
                print("Too small!")
                pass
        except ValueError:
            pass


# Run main function within file
if __name__ == "__main__":
    main()
