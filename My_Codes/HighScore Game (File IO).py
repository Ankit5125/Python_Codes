'''
suppose you have one file named HScore
which contains High Score...

you help the user to play a game...
and geneate new score for the user

if score is greater than HScore then print new HScore in file
'''

import random

def game():
    # you can make any game here i am using user input...
    score = int(input("Enter Your Score : "))
    f = open("HScore.txt", "r+")
    HScore = f.read()

    if score > int(HScore) :
        print("Congratulations !! You Got High Score")
        HScore.write(score)

    else :
        print("Sorry Better Luck Next Time....")

game()