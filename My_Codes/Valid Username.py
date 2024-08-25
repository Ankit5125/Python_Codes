''' 
first you have to take username from user
then check if the username contains more than 10 alphabetical character
then and pnly then username is valid 
otherwize not....
'''

username = input("Enter Your Username : ")

if len(username) < 10 :
    print("Not Valid")
    exit()
    
else :
    count = 0
    for i in range(len(username)):
        if username[i] >= 'a' and username [i] <= 'z' :
            count += 1
        elif username[i] >= 'A' and username [i] <= 'Z' :
            count += 1
    
    if count > 10 :
        print("Done ✅")
    else :
        print("Invalid")
