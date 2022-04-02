# When inheritence occurs beyond 2 level is multilevel
# In this, a child class is inherited by another child class.(creating a chain like strcuture)

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
    print("Employee intializing...")


# 2nd Child Class
class Programmer(Employee):
  company = "Myself"

  def __init__(self):
    print("Programmer intializing...")


objpr = Programmer()
print(objpr.company)
print(objpr.motto)  # inherits from its parent class Employee
print(objpr.name)   # inherits from its grandparent class Person