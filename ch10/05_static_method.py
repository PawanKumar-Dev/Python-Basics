# As we have seen if we want to access methods of a class we need to pass the "self" argument. Since without it objects can't access methods of class

# But what if we don't want to access class methods without the "self". Here we use the static methods

class Person:
  age = 26
  names = "pawan"

  @staticmethod
  def printdetails():
    print("Printing Details")

person1 = Person()
person1.printdetails()
# now this works despite not being having a "self" keyword