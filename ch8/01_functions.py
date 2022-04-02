# Function is a block of code that performs a specific task. It is useful since it can be reused any number of times.

# def -- is the keyword to define a function in Python
# return -- when our function is not directly printing, we return the values that has been calculated(performed) in function.
# arugument -- is the value that is function is reciveing and processing. They are passed inside () brackets. They can be one or many. 

def calculatePercent(marks):
  return (sum(marks)/400)*100

marks = [45, 12, 36, 56]
p = calculatePercent(marks)
print(p)


marks2 = [78, 23, 89, 16]
k = calculatePercent(marks2)
print(k)