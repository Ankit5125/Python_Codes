'''
you have to print table of 2 to 20
each table must be in unique file
'''

for i in range(1,21):
    f = open(f"{i}.txt","w")

    for j in range(1,11):
        f.write(f"{i} * {j} = {i * j}\n")

    print(f"Table of {i} Created Successfully...")
    f.close()
