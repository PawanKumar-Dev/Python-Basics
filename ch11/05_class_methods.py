# Class methods are linked/bound to the class itself. Unlike other methods who are linked to instance of class.
# So if you want to change the property of class itself without creating an instance/object, then we implement class methods

# If try changing class variable salary with normal methods
class Employee:
  name = "pawan",
  salary = 100

  @classmethod                             # called decoraters
  def changeClassSalary(cls, salary):
    cls.salary = salary

  def changeSalary(self, salary):
    self.salary = salary

emp1 = Employee()

# Salary before function changing
print(Employee.salary)
emp1.changeSalary(200)

# We can see Class salary variable is unchanged
print(Employee.salary)

# Now we use the class methods
emp1.changeClassSalary(200)
print(Employee.salary)