# first you have to get string from user...
# then ask for n (repeatation)
# print the first two characters of string for n times
# note that if string length is less then 2 then print string n times

str = input("Enter String : ")
n = int(input("Enter Repeatation : "))

if(len(str) < 2):
    for i in range(n):
        print(str,end="")

else:
    for i in range(n):
        print(str[:2], end="")
