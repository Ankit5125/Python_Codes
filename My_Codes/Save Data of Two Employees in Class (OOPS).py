class programmer:
    
    def __init__(self,name , dept, branch, salary):
        self.name = name
        self.dept = dept
        self.branch = branch
        self.salary = salary
    
    def pdetails(self):
        print(f"Name = {self.name}\nDepartment = {self.dept}\nBranch = {self.branch}\nSalary = {self.salary}")
        

e1 = input("Enter Name of The Employee 1 : ")
d1 = input("Enter Department of the Employee 1 : ")
b1 = input("Enter Branch of the Employee 1 : ")
s1 = int(input("Enter Salary Of the Employee 1 : "))

emp1 = programmer(e1,d1,b1,s1)
print("\n")

e2 = input("Enter Name of The Employee 2 : ")
d2 = input("Enter Department of the Employee 2 : ")
b2 = input("Enter Branch of the Employee 2 : ")
s2 = int(input("Enter Salary Of the Employee 2 : "))

emp2 = programmer(e2,d2,b2,s2)


emp1.pdetails()
print()
emp2.pdetails()
