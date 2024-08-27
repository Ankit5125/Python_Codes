'''
create a class named animal
create a class pets that inheritance animal
create a calss of dog that inheritance pets
create a method to bark the dog...
'''

class animal:
    def __init__(self):
        print("This is Animal Class")
        
class pets(animal):
    def __init__(self):
        super().__init__()
        print("This is Pets Class")
        
class dogs(pets):
    def __init__(self):
        super().__init__()
        print("This is Dogs Class")
        
    def bark(self):
        print("Dog is Barking...")
        
a = dogs()
a.bark()
