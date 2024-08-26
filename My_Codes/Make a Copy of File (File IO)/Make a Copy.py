'''
you have one file named file.txt
you have to copy entire file into another file which have name 'copy'
'''

f = open("file.txt")
fcpy = open("copy.txt" ,  "w")

ls = f.read()

for i in range(len(ls)):
    fcpy.write(ls[i])