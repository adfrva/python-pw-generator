import random

niceWordFile = open("positive-words.txt")
niceWords = niceWordFile.read()

print("Welcome to the password generator\n")
print("Do you want a new password? Type Y or N")
userAnswer = input()
generatedPW = ""

if userAnswer == "Y" or userAnswer == "y":
    generatedPW = generatedPW + random.choice(niceWords)
    print("Heres your password: ", generatedPW)
elif userAnswer == "N" or userAnswer == "n":
    print("goodbye")
else:
    print("Wrong answer")