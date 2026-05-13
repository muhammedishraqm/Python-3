# # THIS PROJECT GENERATE ID CARD

# name = input("enter your full name: ")
# print("LEVEL: 1, 2, 3, 4, 5")
# access = input("enter your access level ")
# temp = float(input("enter your body temp "))
# print("SECURITY PASS : 1 FOR TRUE --AND-- 0 FOR FALSE")
# passs = bool(input("security pass "))

# print(f"AGENT:{name}.\nLEVEL:{access}.\nSTATUS:{passs}")


# # SMART BUDGET TRACKER

# week = float(input("weekly allowance : "))
# food = float(input("food cost : "))
# travel = float(input("travel cost : "))

# total = food + travel
# remain = week - total

# # print(f"total budget :{total} and remaining balance is :{remain}")


# # GRADE CALCULATOR 
# x = int(input("enter your mark: "))

# if x > 50 :
#     print("Enter valid mark, out of 50")
#     exit()

# if 50 >= x > 45 :
#     print("A")
# elif 45 >= x > 35 :
#     print("B")
# elif 35 >= x > 25 :
#     print("C")
# elif 25 >= x > 15 :
#     print("D")
# else :
#     print("F")


# # USER NAME AND PASS
# user = "abc123"
# passs = 321

# x = input("enter your user name: ")
# y = int(input("enter your password: "))

# if user == x and passs == y :
#     print("correct")
# else :
#     print("incorrect")


# # LEAP YEAR CHECK
# y = int(input("Year? "))


# if y%100 == 0 and y%400 == 0:
#     print("LEAPYEAR")
# elif y%4 == 0 :
#     print("LEAPYEAR")
# else:
#     print("NOT")


# # BMI CALCULATOR

# h = float(input("hight: "))
# w = float(input("wieght: "))
# r = w/(h*h)

# if r >= 30 :
#     print("obese")
# elif 29.9 >= r >= 25.0 :
#     print("over")
# elif 24.9 >= r >= 18.5 :
#     print("normal")
# else :
#     print("under")

# # BANK

# balance = 2000
# usern = "abc123"
# passs = 321
# newb = 0

# # AUTHENTICATION
# a = input("user name: ")
# b = int(input("password: "))

# if a == usern and passs == b :
#     x = input("ENQUIRY : \n1.BALANCE \n 2.WITHDRAW ")
#     if x == "1" :
#         print(balance)
#     elif x == "2" :
#         y = int(input("amount: "))
#         if y <= balance and y > 0 :
#             balance = balance - y
#             print(f"withdraw {y} \nbalance {balance}")
#         else :
#             print("invalid amount")
    
# else :
#     print("incorrect, please try again ")


# # GUESSING GAME
# import random as rn

# i = True
# num = rn.randint(1,100)
# while i :
#     x = int(input("enter a number "))
#     if x == num :
#         print("GOOD")
#         print("actual value is: ",num)
#         i = False
#     else :
#         print("LOST")
#         if num > x :
#             print("YOUR GUESSING, LOW")
#         elif num < x :
#             print("YOUR GUESSING, HIGH")
#         print("TRY AGAIN")


# # PRINT N OUTPUT , MUST BE POSITIVE
# n = int(input("n ? "))
# i = 0
# x = True
# while x :
#     if n > 0 :
#         x = False
#         while i < n :
#             print("hai")
#             i = i+1
#     elif n <= 0 :
#         n = int(input("n ? "))


