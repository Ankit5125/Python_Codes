ls = dict()
index = 0



def add(index):
    ask = input("\nEnter Task : ")
    ls[index] = ask
    index += 1
    return index

def reindex():
    temp = {}
    i = 0
    for key in ls:
        temp[i] = ls[key]
        i += 1
    
    ls.clear()
    ls.update(temp)

def remove(index):
    i = int(input("\nEnter Index : "))
    try:
        ls.pop(i)
        print("\nTask Removed Successfully....")
        index -= 1
        reindex()
        
    except KeyError:
        print("\nPlease Enter Valid Index : ")

    return index
    
def mark():
    
    i = int(input("Enter Index : "))
    
    try:
        ls[i] = ls[i] + " ✅ "
    except:
        print("Enter Valid Index")    

    
def edit():
    geti = int(input("\nEnter Index You Want to Edit : "))
    
    try:
        newinput = input("Enter new Task : ")
        ls[geti] = newinput
    except:
        print("\nEnter Valid Index...\n")    

def display():
    print()
    for key, val in ls.items():
        print(f"{key} : {val}")
    print()

print("-" * 50)

while True:
    print("\nEnter Your Choice : \n1 -> Add\n2 -> Remove\n3 -> Mark as Done ✅\n4 -> Edit\n5 -> Display\n0 -> Exit\n")
    
    choice = int(input("\nChoice :"))
    
    if choice == 1:
        index = add(index)
    
    elif choice == 2:
        index = remove(index)
    
    elif choice == 3:
        mark()
        
    elif choice == 4:
        edit()
    
    elif choice == 5:
        display()
        
    elif choice == 0:
        print("\n\nThank You...\n\n")
        exit() 
    
    else:
        print("\nEnter Valid Number...")
        
