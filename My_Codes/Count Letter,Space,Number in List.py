str = input("Enter String :")

letter = int(0)                                              
space = int(0)                                               
number = int(0)                                              
other = int(0)

for i in range(len(str)):
    if (str[i] >= 'A' and str[i] <= 'Z') or  (str[i] >= 'a' and str[i] <= 'z'):
        letter += 1
    elif (str[i] == ' '):
        space += 1
    elif (str[i] >= '0' and str[i] <= '9' ):
        number += 1
    else:
        other += 1

print(f"letter : {letter}\nspace : {space}\nnumber : {number}\nother : {other}")
