# Properties that belong to instances or object indivdaully rather than Class are called Instance Attributes.
# Even though they share same class. Object/ Instance Attributes can be diffrent

class Furniture:
  wood = "Mahagony"

table1 = Furniture
table1.size = "Big"         #"size" here is an instance attribute

table2 = Furniture
table2.size = "Small"
#Again since size is instance attribute it can have diffrent values depending upon its instance/object

# "NOTE:" Instance attribute have higher priority over Class attributes