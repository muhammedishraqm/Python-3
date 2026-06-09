print("---Welcome to Quiz Game---\nEnter 'exit' for quit")


score = 0

is_play = True
while is_play:
    x = input("Do you want to Play: ").lower()
    if x == "yes" :
        print("Okay, let's play!")
        is_play = False
    elif x == "no" :
        print("Bye")
    else :
        print("Enter valid input 'YES' or 'NO' ")

    answer1 = input("What does CPU stand for? ")
    if answer1.lower() == "central processing unit":
        print("Congratzz you Won")
        score += 10
    elif answer1.lower() == "exit":
        print("Bye")
        break
    else :
        print("sorry you Lost")
    


    answer2 = input("What does RAM stand for? ")
    if answer2.lower() == "random access memory":
        print("Congratzz you Won")
        score += 10
    elif answer1.lower() == "exit":
        break
    else :
        print("sorry you Lost")

    


    answer3 = input("What does PSU stand for? ")
    if answer3.lower() == "power supply unit":
        print("Congratzz you Won")
        score += 10
    elif answer1.lower() == "exit":
        break
    else :
        print("sorry you Lost")



    answer4 = input("What does GPU stand for? ")
    if answer4.lower() == "graphics processing unit":
        print("Congratzz you Won")
        score += 10
    elif answer1.lower() == "exit":
        break
    else :
        print("sorry you Lost")


perc = (score / 40) * 100
print(f"Your score is {score}\nand your percentage is {perc}")