# String has 0 based index in Python and we can access this
a = "Pawan"

#accessing 0 position index of variable "a"
print(a[0])

# Even though you can access the character. You are not allowed to modify
# a[0] = "K" --> doesn't work

# String slicing (0:3) --> actually count 0,1,2 only
print(a[0:3])

# this works since Py assume first index as 0
print(a[:4])

# In this case Py assume last index as length of string
print(a[0:])


# Python also support negative index. This is useful when you want to access last character in a unknown length string
# Negative index begins from -1
print(a[-3:-1])


# String characters can skipped as well.
# We just need to pass a 3rd arugment to our slicing
str = "ABCDEFGHIJKL"
print(str[0:5:2])  #with 2 as 3rd argument we skip 1 characters
print(str[0::3])  #with 3 as 3rd argument we skip 2 characters