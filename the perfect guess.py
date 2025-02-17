import random

number = random.randint(1, 100)

player_name1 = input("Hello, What's your name? ")
player_name2 = input("Hello, What's your name? ")
print(f'Okay {player_name1} and {player_name2} I am guessing a number between 1 and 100. Try to guess it!')



number_of_guesses = 0

while True:  
    guess1 = int(input("Enter your guess: "))
    guess2 = int(input("Enter your guess: "))

    if guess1 and guess2 < 1 or guess1 and guess2 > 100:
        print("Please enter a valid number between 1 and 100. Game Over!")
        break


    number_of_guesses += 1
    
    if guess1 < number:
        print('Your guess is too low. Try again!')
    elif guess1 > number:
        print('Your guess is too high. Try again!')
    else:
        print(f'Congratulations {player_name1}! You guessed the number {number} in {number_of_guesses} tries!')

    if guess2 < number:
        print('Your guess is too low. Try again!')
    elif guess2 > number:
        print('Your guess is too high. Try again!')
    else:
        print(f'Congratulations {player_name2}! You guessed the number {number} in {number_of_guesses} tries!')

        break
