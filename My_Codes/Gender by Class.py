class person:
    def __init__(self,gender):
        self.gender = gender

    def pgender(self):
        print(self.gender)

class male(person):
    def __init__(self, gender):
        super().__init__(gender)

class female(person):
    def __init__(self, gender):
        super().__init__(gender)

m = "male"
f = "female"

male(m).pgender()
female(f).pgender()
