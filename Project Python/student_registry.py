import secrets
import string
import time

print("Hello")
time.sleep(3)
student = input("Are you a student [y|n]:  ")
student.lower()
def generate_alphanumeric(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
if student == "y" or "":
    ide = [generate_alphanumeric(5), generate_alphanumeric(5), generate_alphanumeric(5), generate_alphanumeric(5)]
    student_name = input("Enter your student name:  ")
    student_id = input("Enter your Student ID:  ")
    if student_id == "":
        print(f"It appears you dont have a student ID, {student_name}")
        time.sleep(2)
        generate = input("Do you want a student ID? [y|n]: ").lower()
        if generate == "y":
            id = generate_alphanumeric(5)
            ide.append(id)
            print(f"Welcome {student_name}")
            time.sleep(2)
            print(f"Your new student ID is {id}")
        elif generate == "n":
            print("You can no longer participate in this program")
    elif student_id in ide:
        print(f"Alright then, welcome {student_name}")
        print(f"We will register your ID, {student_id}")
    elif student_id not in ide:
        print("ID not registered , please exit the program")
elif student == "n":
    print("Then you have no business here")