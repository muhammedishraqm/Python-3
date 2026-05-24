# ------------VAR--------------
# STR


# #input and output
# name = str(input("whats your name :"))
# print("Hey",name)
# age = int(input("your age: "))
# print("Your age is" , age)


# #combined command and variables 
# print(f"your name is {name} and you are {age} year old")


# # \"---------\"
# print("your name is \"ishraq\"")


# # Remove extra spaces from left and right
# a = "       JOHN & JACOB        "
# print(a)


# a = a.rstrip()                # remove space from right                       
# print(a)

# a = a.strip()                 # remove spaces from both
# print(a)

# a = a.lstrip()                # remove spaced from left
# print(a)


# # capitalize() title() upper() lower()
# b = "python PROGRAMMING"

# b = b.capitalize()          # capital first letter the first word
# print(b)

# b = b.title()               # capital first letter of all word
# print(b)

# b = b.upper()
# print(b)

# b = b.lower()
# print(b)

# b = b.split()               # it split and converted into list contains the splitted items
# print(b)


# INT & FLOAT

# x = 3
# y = 7
# print(x + y)

# a = input("first value: ")
# b = input("second value: ")
# print(a+b)                 # "input" stored as str so it will add 1+2 = 12
# print(int(a)+int(b))       # convert into int, 1+2 = 3

# a = int(input("first value: "))
# b = int(input("second value: "))
# print(a+b)

# a = float(input("first value: "))
# b = float(input("second value: "))

# z = a/b
# n=5                          # decimal of rounding
# w = round(a/b,n)             # round to nearest integer with respect to decimal of "n"

# print(z)
# print(w)

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

