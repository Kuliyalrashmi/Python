#OOPs concepts in Python 
'''
1. Class Definition syntax and how to create an objects of class
2. Instance variables
3. Inheritance and Multiple Inheritance
4. Polynorphism
  -Overloading
  -Overriding
  -Data Hiding
5. Constructors in Python

'''
# Class
class BaseClass:
 # Instance Variable
 x = 5

# Object creation
obj = BaseClass()
print(obj.x)

class Email:
  pass

e1=Email()
e2=Email()
print(type(e1))

class Employee:
  def __init__(self,nm,age):
    self.name=nm
    self.age=age
  def display(self):
    print(self.name)

E1=Employee("Rashmi",20)
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
