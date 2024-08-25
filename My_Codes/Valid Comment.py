# get comment from user...
# check if comment contains specific words like :
# "make a lot of money", "buy now", "subscribe this", "click this"
# if yes then comment is fake....
# else comment if Valid

# Method 1 : 

'''
m1 = "make a lot of money"
m2 = "buy now"
m3 = "subscribe this"
m4 = "click this"

cmt = input("Enter comment : ")

if m1 in cmt or m2 in cmt or m3 in cmt or m4 in cmt :
    print("Fake Comment")

else :
    print("Valid Comment")
    
'''
    
# Method 2 :

ls = ["make a lot of money","buy now","subscribe this","click this"]

cmt = input("Enter comment : ")

for words in ls :
    if words in cmt :
        print("Fake Account")
        exit()
        
print("Valid Comment")
