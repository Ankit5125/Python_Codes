# first you have to take string from user
# than check if string contains 'ls' 
# if yes : then bring ls to the first index

ls = "ls"

str = input("Enter String : ")

ans = ls + str.replace("ls" ,"")

print(ans)
