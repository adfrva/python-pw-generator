import random

print("Welcome to the password generator\n")
print("Do you want a new password? Type Y or N")
userAnswer = input()
generatedPW = ""

if userAnswer == "Y" or userAnswer == "y":
    print("Heres your password: ")
elif userAnswer == "N" or userAnswer == "n":
    print("goodbye")
else:
    print("Wrong answer")