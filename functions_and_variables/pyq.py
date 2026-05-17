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


# def multiple (num1, num2):
#     return num1 * num2

# print(multiple(5,6))

## FUNC AUTH
# x = input("User: ")
# y = input("Pass: ")

# def data(user,pas):
#     if user == x and y == pas :
#         print("YES")
#     else :
#         print("NO")
#     return user,pas

# data("abc123","321")


# def curr(amount):
#     amount = float(amount)
#     print(f"${amount:.2f}")
#     return amount
# curr(10)





# --- ATM FUNCTIONS ---

def bal(balance1):
    """Displays the current balance."""
    print(f"Your balance is: ${balance1:.2f}")

def dep(balance, deposit_amount):
    """Calculates the new balance after a deposit."""
    return balance + deposit_amount

def withd(balance, withdraw_amount):
    """Calculates the new balance after a withdrawal."""
    return balance - withdraw_amount

# --- MAIN CONTROLLER ---

def main():
    # 1. Initialize our local balance variable inside main
    balance1 = 5000 
    is_running = True
    
    while is_running:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Pass the current balance to be printed
            bal(balance1)
            
        elif choice == "2":
            amount = int(input("How much money to deposit: $"))
            # CRITICAL STEP: We catch the returned value to update balance1
            balance1 = dep(balance1, amount)
            print(f"Successfully deposited ${amount}. New balance updated.")
            
        elif choice == "3":
            amount = int(input("How much money to withdraw: $"))
            # Challenge area: We need to update balance1 here too
            balance1 = withd(balance1, amount)
            print(f"Successfully withdrew ${amount}. New balance updated.")
            
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please choose 1-4.")

# This line physically triggers our main program to start running
main()
