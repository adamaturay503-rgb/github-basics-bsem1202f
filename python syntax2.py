try:
    user_age =int(input("please enter your age:"))
    print(f"you are {user_age} years old")
except ValueError:
    print("Invalid input. not a number")

student = input("Please enter your name:")
print(student)
print(f"Good afternoon {student}")