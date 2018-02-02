"""guesser.py, By Javier Ramirez, 12-16-2017
Updated: 2-1-2018
This program has the user guess a number between 1 and 100.
A couple of things I have learned from this project is using the random library, using while loop and
I just recently added a try/exception to the project to catch non-integer
"""
import random

def main():
    print("Guess a number between 1 and 100")
    # random_number = 35 for debugging only
    
    random_number = random.randint(1,100)
    found = False  # flag variable to see
                   #if they guess the right number
    guess = 1
    
    while not found: 
        try:
            user_Guess = int(input("Your guess: "))
            
            if user_Guess == random_number:
                print("You got it!")
                found = True
            elif user_Guess > random_number:
                print("Guess lower!")
                guess += 1
            else:
                print("Guess higher!")
                guess += 1
        except ValueError:
            print('Please enter an integer')
    
    print("Thanks for playing! It took you {} tries!".format(guess))



if __name__ == "__main__":
    main()
