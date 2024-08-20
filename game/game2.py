"""
I’m thinking of a number between 1 and 100...

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and , inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

# Load library
import random

# Main function
def main():
  level = user("Level: ")
  ran_num = ran_int(level)
  while True:
    guess = user("Guess: ")
    if guess < ran_num:
      print("Too small!")
      pass
    elif guess > ran_num:
      print("Too large!")
      pass
    else:
      print("Just right!")
      break

# prompt user for input of positive int
def user(a):
  while True:
    try:
      i = int(input(a))
      if i > 1:
        return i
      else:
        pass
    except ValueError:
      pass

# random
def ran_int(r):
  return random.randint(1, r)

# run main function within script
if __name__ == "__main__":
  main()
