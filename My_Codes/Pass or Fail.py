'''
take marks of subjects from user
if total percentage > 40 then student is passed otherwise Fail

note that each subject must obtain atleast 33 marks inorder to pass
assume total subject are 3 
'''

ls = []
total = 0

for i in range(3):
    m = int(input(f"Enter Marks for Subject {i+1} : "))
    ls.append(m)
    total += m
    
for marks in ls :
    if marks < 33 :
        print("Fail")
        exit()

if total / 3 >= 40 :
    print("Pass")
    
else :
    print("Fail")    
