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

#-------------------- IF  ELIF  ELSE ----------------------------

# # IF CHECK THE COMPLETELE CONDITION

# x = input("X: ")
# y = input("Y: ")
# if x < y:
#     print("x is less than y")
# if x > y :
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")


# # ELIF CHECK ONLY IF IS FALSE
# x = input("X: ")
# y = input("Y: ")
# if x < y:
#     print("x is less than y")
# elif x > y :
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")


# # ELSE CHECK ONLY IF AND ELIF BOTH ARE FALSE
# x = input("X: ")
# y = input("Y: ")
# if x < y:
#     print("x is less than y")
# elif x > y :
#     print("x is greater than y")
# else:
#     print("x is equal to y")

# ---------------------  LOOP  -------------------------------

# stu = ["hey","hello","hou"]
# for i in stu :
#     print(i)

# i = 0
# while i < 3 :
#     print(i)
#     i = i + 1

# ---------------------- FUNCTION -----------------------------