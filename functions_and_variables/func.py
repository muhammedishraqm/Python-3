# ---------------------- FUNCTION -----------------------------

# def square(num):
#     print(num * num)

# # or 

# def square(num):
#     return num * num


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


# def off():
#     print("start")
#     print("work")
#     print("stop")
# off()


# def func_name(-PARAMETER-)
#     print(---------)
# func name(-ARGUMENTS-)


# def lowerr(x):
#     print(x.strip().lower())
# lowerr("     hEYYYY          ")

# def names(first,last,country):
#     firstn = first.strip().lower()
#     lastn = last.strip().lower()
#     coun = country.strip().lower()
#     full = firstn+" "+lastn+" from "+coun
#     print(full)

# names("john","davis","India")                                   #POSITIONAL ARG   (Order Matters)
# names(first = "john",last = "davis",country = "India")          #KEYWORD ARG      (Safe than POSITIONAL ARG)           














# # --- ATM FUNCTIONS ---

# def bal(balance1):
#     """Displays the current balance."""
#     print(f"Your balance is: ${balance1:.2f}")

# def dep(balance, deposit_amount):
#     """Calculates the new balance after a deposit."""
#     return balance + deposit_amount

# def withd(balance, withdraw_amount):
#     """Calculates the new balance after a withdrawal."""
#     return balance - withdraw_amount

# # --- MAIN CONTROLLER ---

# def main():
#     # 1. Initialize our local balance variable inside main
#     balance1 = 5000 
#     is_running = True
    
#     while is_running:
#         print("\n--- ATM MENU ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             # Pass the current balance to be printed
#             bal(balance1)
            
#         elif choice == "2":
#             amount = int(input("How much money to deposit: $"))
#             # CRITICAL STEP: We catch the returned value to update balance1
#             balance1 = dep(balance1, amount)
#             print(f"Successfully deposited ${amount}. New balance updated.")
            
#         elif choice == "3":
#             amount = int(input("How much money to withdraw: $"))
#             # Challenge area: We need to update balance1 here too
#             balance1 = withd(balance1, amount)
#             print(f"Successfully withdrew ${amount}. New balance updated.")
            
#         elif choice == "4":
#             print("Thank you for using the ATM. Goodbye!")
#             is_running = False
#         else:
#             print("Invalid choice. Please choose 1-4.")

# # This line physically triggers our main program to start running
# main()

