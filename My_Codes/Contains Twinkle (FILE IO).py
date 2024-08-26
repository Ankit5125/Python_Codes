''' 
you are given a file poems.txt
which have poems written... 
check if file contains word 'twinkle'
'''

f = open("poems.txt")

lines = f.readlines()

if "twinkle" in lines :
    print("File Contains word 'Twinkle'")
else :
    print("File Does not Contains 'Twinkle'")