'''
you have to count simple intrest and intrest 
by getting info from user
'''

p = int(input("Enter Initial Amount : "))
r = float(input("Enter Rate "))
n = int(input("Enter Total Year : "))

def s_intrest(p,r,n):
    print((p * r * n)/100)

def intrest(p,r,n):
    print(p*((1 + r/100)**n))

s_intrest(p,r,n)
intrest(p,r,n)
