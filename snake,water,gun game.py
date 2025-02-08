import random
'''
1 = snake
2 = water
3 = gun
'''
computer = random.choice([1,2,3])
player = input("Enter your choice: ")
dictionary = {"s":1,"w":2,"g":3}
revdictionary = {1:"snake", 2:"water", 3:"gun"}
you = dictionary[player]

print(f"You chose {revdictionary[you]}\ncomputer chose {revdictionary[computer]}")

# if computer == you:
#     print("its a draw")

# else:
#     if(computer==1 and you == 3):         
#         print("you win!")
#     elif(computer==1 and you == 2):        
#         print("You lose!")
#     elif(computer==2 and you == 1):        
#         print("You win!")
#     elif(computer==2 and you == 3):         
#         print("You lose!")
#     elif(computer==3 and you == 2):         
#         print("You win!")
#     elif(computer==3 and you ==1 ):           
#         print("You lose!")
#     else:
#         print("Daya kuch to gadbad hai")
if computer == you:
    print("It's a tie!")
elif (computer - you) % 3 == 1:
    print("You win!")
else:
    print("You lose!")
