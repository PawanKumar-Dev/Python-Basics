# Properties that belong to a Class rather that object are Class Attributes.
# Class Attributes represent the class. And they can be accessed via class too.

class Furniture:
  wood = "Mahagony"

table1 = Furniture()                # object of Furniture class
print(Furniture.wood)               # accessing class attributes
Furniture.wood = "Sandlewood"       # changing a class attribute
print(Furniture.wood)