'''
create 2 classes 2d vector and 3d vector
call the 3d vector and print value of 2d vector using constructor
'''

class v2d:
    def __init__(self,x = 5,y = 3):
        self.x = x
        self.y = y
        
class v3d(v2d):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

obj = v3d(5,3,3)
print(obj.z)
print(obj.x)
