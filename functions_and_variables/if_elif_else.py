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
