#Inheritance
class Employee:
    bonus=2000
    def display(self):
        print("this is employee class method")

class Manager(Employee):
    bonus1=6000
    def show(self):
        print("this is manager class method")

E1=Employee()
M1=Manager()

E1.display()
M1.show()
M1.display()
print(M1.bonus)
class Class1:
    def display(self):
        print("In Class1")
class Class2(Class1):
    def display(self):
        print("In Class2")
class Class3(Class1):
    def display(self):
        print("In Class3") 
class Class4(Class3, Class2):
    pass 
obj = Class4()
obj.display()