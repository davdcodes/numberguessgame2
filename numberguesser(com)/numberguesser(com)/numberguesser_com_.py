import random

numdiff = "n"
replay = "y"
highscore = 0

print("--------------------------------------------------------------------------------------------------------------------------------------")

print("Hey, let's play the number guessing game!")
print("But since you always have to be the one to guess the number, how about I try this time!")
print("Okay, here's what we'll do!")
print("I'll guess a number between 1 and 100, and you can tell me if your number is higher (h) or lower (l)! Or, if I guess right, just give me a 'e'! ")
print()

while replay != "q":
    numlow = 1
    numhigh = 100
    guesses = 1

    answer = input("How about you think of a number, and then enter '1' once you've got one! ")
    while answer != "1":
        answer = input("Ooo, that's not a '1'! Did you make a mistake? Make sure to enter '1' once you think of a number so we can play! ")

    print()

    numguess = random.randint(numlow,numhigh)
    numdiff = input("Okay, I'll guess that your number is " + str(numguess) + ". Was I close? (h|l|e) ")

    while numdiff != "e":
        if numdiff == "h" or numdiff == "l":
            if numdiff == "l":
                numhigh = numguess - 1
            elif numdiff == "h":
                numlow = numguess + 1
            numguess = random.randint(numlow,numhigh)
            numdiff = input("Okay, I'll guess that your number is " + str(numguess) + ". Was I close? (h|l|e) ")
            guesses += 1
        else:
            numdiff = input("Let's try answering with one of the prompts! Is your number higher, lower, or equal to " + str(numguess) + "? ")

    print()
    if guesses <= 5:
        print("No way, I got it? I can't believe you picked " + str(numguess) + ", what an easy number!")
        print("I barely even took " + str(guesses) + " tries to figure it out!")
    elif guesses <= 10:
        print("Oh wow, that was a good number! I wouldn't have guessed you'd pick " + str(numguess) + "! ")
        print("It even took me " + str(guesses) + " to get that one!")
    else:
        print("Finally! I didn't think I'd ever get it, " + str(numguess) + " was a hard number!")
        print("It took a while, but I got there after " + str(guesses) + " attempts!")
    
    if (guesses < highscore) or (highscore == 0):
        highscore = guesses 
        print()
        print("Wow! " + str(highscore) + " is a new record for me! I'll try to guess the next number in even less attempts!")

    print()
    replay = input("Well, do you you wanna play again?? ('q' to quit, any key to continue) ")
    print("--------------------------------------------------------------------------------------------------------------------------------------")


print("Awww, that was fun too! Well, thanks for playing!")