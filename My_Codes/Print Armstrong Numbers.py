def isArm(num):
    n = len(str(num))
    s = 0
    
    for i in str(num):
        s += int(i) ** n
    
    if s == num :
        return True 
    
    return False        

# lastnum = int(input("Enter range : "))

lastnum = 2000000

for i in range (1,lastnum):
    if isArm(i) :
        print(i)
