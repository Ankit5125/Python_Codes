# first take num input
# then print character vise '@'
# exa : num = 123
# @
# @@
# @@@

num = int(input("Enter Number : "))
# 12345
ls = []

while(num > 0):
    ls.append(num % 10)
    num = num // 10
# ls = 5 4 3 2 1

ls.reverse()
# 1 2 3 4 5

for index in ls:
    for i in range(1 , index+1):
        print("@",end="")
    print()
