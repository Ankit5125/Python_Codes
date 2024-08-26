import random

options = {
    "Rock":1,
    "Paper":2,
    "scissor":3
}

while True :
    print("Enter Choice : \n 1 -> Play \t 0 -> Exit")
    go_ahead = int(input("Choice : "))

    if go_ahead == 1 :
        comp = random.randint(-1,2)
        print("What You Want to Choose ? :")

        you = int(input("\n1 -> Rock\n2 -> Paper\n3 -> Scissor \nChoice : ")) 
        print(f"Computer Have Choosen {options[comp]}")
        print(f"You Have Choosen {options[you]}")

    elif go_ahead == 0 :
        exit()

    else :
        print("Enter Valid Choice...\n")