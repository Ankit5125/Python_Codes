# get friends name and their favourite subject
# print them accordingly name and subject 
# try thinking Map (Dictionary)

frd = int(input("How many Friends Do You have ? : "))

dictionary = {}

for i in range(frd):
    name = input("Enter Unique Name : ")
    sub = input("Enter his Favourite Subject : ")
    
    # dictionary.update({name:sub})
    dictionary[name] = sub
    
print(dictionary)
