# Recursion function are func who call themselves.
# They are used mostly for mathematical formulas like factorial.

# recursion function
def factorial(n):
  if(n == 1 or n == 0):
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))