# ------------------------- FILE I/O ----------------------------
'''
| Mode | Meaning         |
| ---- | --------------- |
| `r`  | Read            |
| `w`  | Write           |
| `a`  | Append          |
| `x`  | Create new file |
| `rb` | Read binary     |
| `wb` | Write binary    |


Suppose "data.txt" file contains:
Hello
Python


---------   read()    ----------
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


Output:
Hello
Python


---------   readline()    ----------
file = open("data.txt", "r")

print(file.readline())
print(file.readline())
file.close()

Output:
Hello
Python


---------   readlines()    ----------
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

Output:
['Hello\n', 'Python']


---------   Writing Files   ----------

file = open("data.txt", "w")
file.write("Welcome to Python")
file.close()

File content:
Welcome to Python


---------   Appending Files    ----------

file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()

File content:
Welcome to Python
New Line Added


-------------------Best Method. with Statement----------------------


with open("data.txt", "r") as file:
    content = file.read()
    print(content)

    

---------------------- PYQ --------------------------------

with open("new_student.txt","w") as file:
    x = file.write("Alice")
    print(x)

-------------  

students = ["Alice", "Bob", "Charlie"]

for i in students :
    file = open("new_student.txt","a")
    file.write(f"\n{i}")

-------------

students = ["Alice", "Bob", "Charlie"]

for i in students :
    with open("new_students.txt","a") as file:
        x = file.write(f"\n{i}")

------------
count = 0
with open("story.txt","r") as file :
    x = file.read().lower().strip().split(" ")
    for i in x :
        if i == "the":
            count += 1
            count +1
    print(count)

-----------------

with open("records.csv","w") as file :
    file.write(f"Name,Age,Grade\n")
    for i in range(3):
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        file.write(f"{name},{age},{grade}\n")
    
-----------------

with open("records.csv","w") as file :
    file.write(f"Name,Age,Grade\n")

    while True :
        name = input("Name: ")
        if name == "exit":
            break
        age = int(input("Age: "))
        grade = input("Grade: ")

            
        file.write(f"{name},{age},{grade}\n")

------------------





'''



