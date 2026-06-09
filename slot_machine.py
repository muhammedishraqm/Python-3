# HANDLE USER INPUT AND BANKING
import random as rd

symbol_count = {
        "A":2, 
        "B":4, 
        "C":6, 
        "D":8
    }

Rows = 3
Cols = 3




def dep():
    dep = int(input("How much for depoiste: \n"))
    return dep

def line():
    line = int(input("line : 1, 2, 3\n"))
    return line

def bet():
    bet = int(input("How much you want to BET per line: \n"))
    return bet

def main():
    is_true = True
    while is_true :
        balance = dep()
        if balance > 0:
            is_true = False 
        else :
            print("Enter the valid amount\n")
            is_true = True

    is_lines = True
    while is_lines :
        lines = line()
        if lines == 1 or lines == 2 or lines == 3:
            is_lines = False
        else:
            print("Enter the valid amount\nMust be 1, 2, 3\n")


    is_bet = True
    while is_bet:
        user_amount = bet()
        total_amount = lines * user_amount
        if total_amount <= balance:
            print(f"Your Total betting amount is :{total_amount}")
            break

        else :
            print(f"Enter the valid amount\nYou have only {balance}")









    








main()