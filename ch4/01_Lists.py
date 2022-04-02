# Lists in Py
#======================

# Lists are variable which can store/hold multiple values (they are like indexed array)
# We use [] brackets for lists
# List items can be diffrent types as well

a = ["hey", 45, True, 78]
print(a)


# Just like String literals, Lists index starts from 0 to n-1(n is length)
print(a[0])


# Unlike Strings, we can change values in Lists
print(a)
a[0] = "Hello"
print(a)