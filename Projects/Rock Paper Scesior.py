import random

options = {1: "Rock",2 : "Paper",3 : "Scissor"}


def winner(comp,user):
    if options[comp] == options[user] :
        print("\nDraw")
        
    elif options[comp] == options[1] : 
        if options[user] == options[2] :
            print("\nYou Wins")
        else:
            print("\nComputer Wins")

    elif options[comp] == options[2] :
        if options[user] == options[1] :
            print("\nComputer Wins")
        else :
            print("\nYou Wins")

    else :
        if options[user] == options[1] :
            print("\nYou Wins")
        else :
            print("\nComputer Wins")
    
while True :
    print("Enter Your Choice : ")
    go_ahead = int(input("\n1 -> Play \n0 -> Exit\nChoice : "))
    
    if go_ahead == 1:
        
        comp = random.randrange(1,4)
        
        print(f"Enter Your Choice : \n 1 = {options[1]}\n 2 = {options[2]}\n 3 = {options[3]}\n")
        you = int(input("\nEnter Your Choice : "))
        
        print(f"Computer Choice = {options[comp]}\nYour Choice = {options[you]}")
        
        winner(comp,you)
        print("-" * 40)
        
    elif go_ahead == 0:
        exit()
        
    else :
        print("Enter Valid Choice...\n")