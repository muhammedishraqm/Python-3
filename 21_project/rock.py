import random

choices = ["rock", "paper", "scissors"]
choice = random.choice(choices)
print(choice)

com_win = 0
user_win = 0


while True :
    print("rock", "paper", "scissors")
    choice = random.choice(choices)
    user = input("Say :").lower()
    print(choice)

    if user == "exit":
        break

    if user == "rock" and choice == "rock":
        user_win += 1
        com_win += 1
    if user == "rock" and choice == "paper":
        com_win += 1 
    if user == "rock" and choice == "scissors":
        user_win += 1 


    if user == "paper" and choice == "paper":
        user_win += 1
        com_win += 1
    if user == "paper" and choice == "rock":
        user_win += 1 
    if user == "paper" and choice == "scissors":
        com_win += 1 

        
    if user == "scissors" and choice == "paper":
        user_win += 1
    if user == "scissors" and choice == "rock":
        com_win += 1 
    if user == "scissors" and choice == "scissors":
        user_win += 1
        com_win += 1




print(f"COMPUTER: {com_win},USER: {user_win}")


