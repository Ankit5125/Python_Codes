ls = dict()
index = 0 

def add(index):
    ask = input("\nEnter Task : ")
    ls[index] = ask
    index += 1
    return index
    
def remove(index):
    i = int(input("\nEnter Index : "))
    try :
        ls.pop(i)
        index -= 1
        print("\nTask Removed Succesfully....")
    except:
        print("\nPlease Enter Valid Index : ")
        
    return index
        
def display():
    print()
    for mykey,myval in dict.items():
        print(f"{mykey} : {myval} ")
    print()

print("-" * 50)
        
while True :
    print("\nEnter Your Choice : \n1 -> Add\n2 -> Remove\n3 -> Edit\n4 -> Display\n0 -> Exit\n")
    
    choice = int(input("\nChoice :"))
    
    if choice == 1:
        index = add(index)
    
    elif choice == 2:
        index = remove(index)
    
    elif choice == 3:
        pass
    
    elif choice == 4:
        index = display()
        
    elif choice == 0:
        print("\n\nThank You...\n\n")
        exit() 
    
    else :
        print("\nEnter Valid Number...")   
