# Solving our programming problems with making "Objects" is very popular. And this approach is called Object Oriented Programming.

# OOPs is a design pattern just like POP(Procedural Oriented Programming)
# But OOPs follow the DRY(Don't Repeat Yourself) princple.i.e. it focuses on reusable code

# CLASS
# Class is a blueprint for creating your objects.
# It holds Methods and variables. Which are inherited by Objects when instianted
# Class is written in "PascalCase".

# HumanBeing is class. And company is variable of this class.
class HumanBeing:
  company = "Google"


# OBJECT
# Object is instantiantion of Class. While Class acts like a blueprint it allocates no memory. Memory allocation only happens when a object is made using that class-- called Instantiation.

# Creating an object
pawan = HumanBeing()

# Objects can access all methods of class without bothering the user about its details. This is abstraction of OOPs. It create a layer of abstraction.
# Encapsulation means we organize or encapsulte variable and methods of one functionality together.

# Both Ecapsulation and Abstraction improve maintainability of your code.