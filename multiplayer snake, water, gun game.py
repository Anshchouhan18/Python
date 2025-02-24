import getpass

dictionary = {"s": 1, "w": 2, "g": 3}
revdictionary = {1: "Snake", 2: "Water", 3: "Gun"}

print("Choices: (s)nake, (w)ater, (g)un")

player1 = getpass.getpass("Player 1, enter your choice (s/w/g): ")
while player1 not in dictionary:
    player1 = getpass.getpass("Invalid choice. Choose (s/w/g): ")
 
player2 = getpass.getpass("Player 2, enter your choice (s/w/g): ")
while player2 not in dictionary:
    player2 = getpass.getpass("Invalid choice. Choose (s/w/g): ")

p1 = dictionary[player1]
p2 = dictionary[player2]

print(f"\nPlayer 1 chose: {revdictionary[p1]}")
print(f"Player 2 chose: {revdictionary[p2]}")

if p1 == p2:
    print("It's a draw!")
elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
