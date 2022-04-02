# Inheritence can be 3 major type:
# 1. Single Inheritence: It's simple when "one parent class" is inherited by "one child class".
# 2. Multiple Inheritence: When a single child class inherits muliple parents.

# Example of Multiple Inheritence
class Employee:
  company = "Google"
  salary = 100

class Freelancer:
  company = "Upwork"
  salary = 80


class Designer(Employee, Freelancer):       # inheriting here
  name = "Pawan"

  def getDetails(self):
    print(f"Hi this is {self.name} who is freelancer in {self.company}")


obj = Designer()
obj.getDetails()

# we get company as google becoz Google written before Freelancer when inheriting