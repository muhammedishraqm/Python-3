# ---------------------  LOOP  -------------------------------

# stu = ["hey","hello","hou"]
# for i in stu :
#     print(i)

# i = 0
# while i < 3 :
#     print(i)
#     i = i + 1


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


# # EXPENSE ANALYSER

# exp = [225,335,332,444,533,77,86,4,788,994,224]
# lenn = len(exp)
# a=0
# for i in exp :
#     a=a+i
# b = a / lenn
# print("Your avg expense:",b)


# x = 0
# for i in exp :
#     if x < i :
#         x = i
# print("your highest expense:",x)

# # PYRAMID BUILDERS
# x=4
# i=0
# while i < x+1 :
#     print("*" * i)
#     i += 1
