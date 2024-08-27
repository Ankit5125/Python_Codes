num = int(input("Enter Last Number : "))
ans = 0

''' 
Method 1 : 

for i in range (num+1) :
    ans = ans + i
        
print(ans)        

'''

'''
Method 2 : 
'''

print(sum(range(num+1)))


'''
Method 3 : 
'''

print(num * (num + 1) / 2)