# all you have to do is....
# take 'n' from user (obviously as a String)
# print n + nn + nnn
# exam -> n = 5 
# 5 + 55 + 555 = 615

num = int(input("Enter N : "))

nn = int(str(num) + str(num))
nnn = int(str(nn) + str(num))

print(num + nn + nnn)
