import random as rd


def roll2():
    count1 = 0
    count2 = 0
    while True:
        u = input("PLAYER 1: Move\nY or N\n").lower()
        if u == "y":
            x = rd.randint(1,6)
            count1 += x
            print(f"Player 1: {count1}")

            y = input("PLAYER 2: Move\nY or N\n").lower()
            if y == "y":
                y = rd.randint(1,6)
                count2 += y
                print(f"Player 2: {count2}")
                if count1 >= 50 or count2 >= 50:
                    if count1 > count2:
                        print("Player 1 WON")
                        break
                    elif count2 > count1 :
                        print("Player 2 WON")
                        break
                    else :
                        print("Null")
                        break
        elif u == "n":
            print(f"Player 1 : {count1}\nPlayer 2 : {count2}")
            break
        elif count1 >= 50 or count2 >= 50:
            if count1 > count2:
                print("Player 1 WON")
                break
            elif count2 > count1 :
                print("Player 2 WON")
                break
            else :
                print("Null")
                break


        else:
            print("Invalid select either Y or N")


def roll4():
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    while True :
        a = input("PLAYER 1: Move\nY or N\n").lower()
        if count1 >= 50 or count2 >= 50 or count3 >= 50 or count4 >= 50 :
            print("WON")
            if max(count1,count2,count3,count4) == count1:
                print("Player 1 WON")
                if max(count1,count2,count3,count4) == count2:
                    print("Player 2 WON")
                    if max(count1,count2,count3,count4) == count3:
                        print("Player 3 WON")
                        if max(count1,count2,count3,count4) == count4:
                            print("Player 4 WON")
                            break

        elif a == "y":
            x = rd.randint(1,6)
            count1 += x
            print(f"Player 1: {count1}")
            b = input("PLAYER 2: Move\nY or N\n").lower()
            if b == "y":
                y = rd.randint(1,6)
                print(f"Player 2: {count2}")
                count2 += y
                c = input("PLAYER 3: Move\nY or N\n").lower()
            elif b == "n":
                break
            else :
                print("Invalid select either Y OR N ")
                if c == "y":
                    z = rd.randint(1,6)
                    count3 += z
                    print(f"Player 3: {count3}")
                    d = input("PLAYER 4: Move\nY or N\n").lower()
                elif c == "n":
                    break
                else :
                    print("Invalid select either Y OR N ")
                    if d == "y":
                        q = rd.randint(1,6)
                        count4 += q
                        print(f"Player 4: {count4}")
                    elif d == "n":
                        break
                    else :
                        print("Invalid select either Y OR N ")


        elif a == "n":
            print("THANK YOU")
            break
        else :
            print("Invalid select either Y OR N ")





    




while True:
    num_plyr = input("How many players : 2 or 4 ")
    if num_plyr == "2":
        roll2()
        break
    elif num_plyr == "4":
        roll4()
        break
    else :
        print("Invalid, enter either 2, 4")
