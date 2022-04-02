# Function are divided into 2 main category:
# 1. Built-in: these are function baked in Python itself. E.g., print(), sum()
# 2. User-defined: these function are defined by us

# Example of user-defined function(with 1 argument)
def greet(name):
  print("Good Morning, " + name)

greet("Pawan")


# Function with multiple argument
def doSum(a, b):
  print(a+b)

doSum(5, 4)

# Function with default value for argument. This works in case a value for argument is missing when calling the function
def aftnGreet(name = "Stranger"):
  print("Good Afternoon, " + name)

aftnGreet()