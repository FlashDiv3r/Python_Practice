# Written by: Catlin Rehders for submission on 06/25/2021 
# Adapted from template provided in UTK-COSC111 by: Stephen Marz
# This program randomly selects a number greater than -50 but less 
# than 50 then loops through user input guesses, providing hints, 
# until the user guesses correctly.
from random import randint

def guess(user_guess, correct_num):
    # Checks to see if the guessed number is greater than the random number
    if user_guess > correct_num:
        # Gives hint to user to guess a lower number next time
        print("Your guess is too high!")
        # Loops back to allow user to guess another number
        return False
    # Checks to see if the guessed number is less than the random number
    elif user_guess < correct_num:
        # Gives hint to user to guess a higher number next time 
        print("Your guess is too low!")
        # Loops back to allow user to guess another number
        return False
    # Executes only if the user's guess is correct
    else:
        # Tells the user that they guessed correctly 
        print("YOU GOT IT!")
        # Ends program because user guessed the correct number
        return True

if __name__ == "__main__":
    num = randint(-50, 50)
    while True:
        user_guess = int(input("Enter your guess: "))
        if guess(user_guess, num) == True:
            break
        
