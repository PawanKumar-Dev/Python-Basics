# List Methods
#==================

# In python there are two types of methods(or functions)
# 1. Those who returns somethings
# 2. Those who don't returns anything

# list.sort() --> sorts our list
numbers = [1, 8, 3, 9, 24, 16]
print(numbers)
numbers.sort()
print(numbers)


# list.reverse() --> reverse our list
numbers.reverse()
print(numbers)


# list.append() --> add item to end of our list
numbers.append(45)
print(numbers)


# list.insert(index, value) --> add item at given index position
numbers.insert(2, 99)
print(numbers)


# list.remove(value) --> removes the given value from list
numbers.remove(99)
print(numbers)