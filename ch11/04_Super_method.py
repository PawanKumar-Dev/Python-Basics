# Super method allows us to access access methods of Super class(its immediate parent class) into child class
# It's widely used with __init__ constructor method to create a calling chain of constructor
# syntax: super().anymethod()

# Base Class
class Person:
  name = "pawan"

  def __init__(self):
    print("Person intializing...")


# 1st Child Class
class Employee(Person):
  company = "FreeLancer"
  motto = "Be Free"

  def __init__(self):
    super().__init__()
    print("Employee intializing...")


# 2nd Child Class
class Programmer(Employee):
  company = "Myself"

  def __init__(self):
    super().__init__()
    print("Programmer intializing...")


pr = Programmer()