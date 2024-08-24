# take single character from user 
# then check and print character is vowel or consonant

c = input("Enter Character : ")

if len(c) > 1 :
    print("Enter 1 Character....")

else :
    ls = ['a','e','i','o','u']
    if c in ls :
        print("is Vowel")
    else:
        print("Constatant")
