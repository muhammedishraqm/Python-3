print("------Welcome-----")

import random

while True :
    limit = int(input("Enter maximum number that for guessing\n"))
    if limit > 0 :
        break
    else :
        print("Enter valid limit\nmust be greater than ZERO ")

random_int = random.randint(1, limit)

count = 0
while True :
    count += 1
    guess = int(input("Guess your number :"))
    m = random_int - guess
    if random_int == guess :
        print("You won")
        break
    elif m > 0 :
        print("You guessing BELOW ")
    elif m < 0 :
        print("You guessing ABOVE ")


if count < 2 :
    print("A grade")
elif 2 <= count < 4:
    print("B grade")
elif 4 <= count < 6:
    print("C grade")
else :
    print("D grade")

