# self refers to the instance of that class. It's part of dry concept.

'''
class Person:
  age = 26
  nam = "pawan"

  def printdetails():
    print("Printing Details)

person1 = Person()
person1.printdetails()
'''

# Give us error: printdetails() takes 0 positional arguments but 1 was given
# this happens becoz when we call our method using an object or instance we are doing this: Person.printdetails(person1)
# Meaning we are passing a argument which is the instance itself.
# And since we cannot pass each instance into function, we use the "self".
# "self" automatically replace itself with object/instance and allow the code to run smoothly

class Person:
  age = 26
  names = "pawan"

  def printdetails(self):
    print("Printing Details")

person1 = Person()
person1.printdetails()