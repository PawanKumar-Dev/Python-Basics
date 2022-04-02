# Inheritence is oops concept which allow a child class(derived class) to inherit variables and methods of Parent class(Base Class)
# This allow Child class to have reduced code and more functionality. Usage of Dry concept.

# =============================
# Base Class or Parent Class
class Cpus:
  generation = "5th"

  def getCpuDetails(self):
    print(f"This CPU is generation: {self.generation}")


# ==============================
# Child Class or Derived Class
# we inherit class by passing it inside the parenthesis of class and passing its name
class Acer(Cpus):
  company = "Acer"
  model = "E7"

  def getPcDetails(self):
    print(f"This PC is from company: {self.company} and has model as: {self.model}")


newpc = Acer()
newpc.getCpuDetails()
newpc.getPcDetails()

# Even though Acer had no such method as getCpuDetails() we still able to use it becoz Acer has inherited it from parent class Cpus.
# And we can even override the methods of Parent class, if we give child class methods the same name