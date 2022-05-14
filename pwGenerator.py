import random

niceWordFile = open("positive-words.txt")
niceWords = niceWordFile.read()
randNum = random.randint(0,25)

print("Welcome to the password generator\n")

userContinue = 1

while userContinue==1:
    print("Do you want a new password? Type Y or N")
    userAnswer = input()
    generatedPW = ""
    if userAnswer == "Y" or userAnswer == "y":
        generatedPW = niceWords[randNum]
        print("Heres your password: ", generatedPW)
        generatedPW = ""
    elif userAnswer == "N" or userAnswer == "n":
        userContinue == 0
        print("goodbye")
        continue
    else:
        print("Wrong answer")