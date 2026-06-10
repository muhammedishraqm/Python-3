while True:
    user = input("\nWELCOME TO PASSWORD MANAGER\nN: Add NEW Pass\nV: VIEW Existing pass\nQ: Quit\n").lower()
    if user == "q":
        print("Thank You For Comming")
        break
    elif user == "n":
        with open("Password.txt","a") as file :
            #file.write("usern, passw\n")
            usern = input("Enter User Name: ")
            passw = input("Enter Password: ")
            file.write(f"{usern}|{passw}\n")
            print(f"You added {usern} and {passw} to PASSWORD MANAGER\nTHANK YOU FOR COMMING")
    elif user == "v":
        with open("Password.txt","r") as file:
            for i in file.readlines():
                data = i.rstrip()
                user,passs = data.split("|")
                print(f"User: {user}, Pass: {passs}")
    else :
        print("Invalid\nN, V, Q")
