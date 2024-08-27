'''
you hacve to take info from user...
and then print them in new Lines
'''

def details(name,address,number):
    name = name
    address = address
    number = number

    print(f"Name : {name}\nAddress : {address}\nNumber : {number}")

name = input("Enter Your Name : ")
address = input("Enter Your Address : ")
number = int(input("Enter Your number : "))

details(name,address,number)