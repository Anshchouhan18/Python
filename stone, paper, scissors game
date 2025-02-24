import random
'''1 = stone
   2 = paper
   3 = scissors(k)'''
computer = random.choice([1,2,3])
player = input("Enter your choice (s for stone, p for paper, k for scissors): ")
dictionary = {"s":1, "p":2, "k":3}
revdictionary = {1:"stone", 2:"paper", 3:"scissors"}

try:
    you = dictionary[player.lower()]
    
    if computer == you:
        print(f"It's a tie! computer chose {revdictionary[computer]}")
    elif (you - computer) % 3 == 1:
        print(f"You win! computer chose {revdictionary[computer]}")
    else:
        print(f"You lose! computer chose {revdictionary[computer]}")
except KeyError:
    print("Invalid input! Please use s, p, or k")
