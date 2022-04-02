# __init__ is a constructor method which runs automatically when an object/instance of class is created.
# Just like other methods we use "self" argument. But it can take other arguement too
class Person:
  personname = "Raju"

  def __init__(self):
    print("Constructor is running!")

  def printpersonname(self):
    print(self.personname)

# When creating object(instantianting)
person1 = Person()


#=======================================================
# Constructor is useful when you want to intialize some values when creating an object and you need not to call any method explicitly
class Fruits:
  benefit = "Healthy"

  def __init__(self, fruitname, fruitprice, fruitseason):
    self.fruitname = fruitname
    self.fruitprice = fruitprice
    self.fruitseason = fruitseason
    print("Fruit Created!")

  def getfruitdetail(self):
    print("Fruit name is ", self.fruitname)
    print("Fruit price is Rs.", self.fruitprice)
    print("This fruit season is ", self.fruitseason)

apple = Fruits("Apple", 100, "Winter")
apple.getfruitdetail()