# Property decorator are methods/functions that represnt like properties of a class. But unlike properties which are hard coded. These property decorator can be dynamic in nature.

class Employee:
  company = "Paytm"
  salary = 5600
  salaryBonus = 550
  # Here we can set a property of total salary = salary + salarybonus
  # But since salaryBonus can be changed in future, we want a dynamic property of total salary

  
  @property                                     # also called property getter function
  def totalSalary(self):
    return self.salary + self.salaryBonus

  
  @totalSalary.setter                           # also called property setter function
  def totalSalary(self, value):
    self.salaryBonus = value - self.salary



# now we treat totalSalary as property not a function
emp = Employee()
print(emp.totalSalary)

# but what if we want to change this property: then we implement a setter function which manipulate values of other properties to set our fake property correct

emp.totalSalary = 5800
print(emp.salary)
print(emp.salaryBonus)