# get number of names from user
# if names start with 's' then print it...

count = int(input("How many Persons are You : "))

names = []

for i in range(count):
    names.append(input(f"Enter name of the person {i+1} : "))

for name in names:
    if name[0] == 's' :
        print(name)
