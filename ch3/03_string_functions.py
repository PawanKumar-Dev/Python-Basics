# String Functions
#====================

# len() to calculate the length of a string
str = "This is a string ending"
print(len(str))

# string.endswith("chkingstring")
# Checks whether a string is ending with particular string we are searching 
# Return a true or false
print(str.endswith("ing"))  #in this case true


# string.count("charcter") -- Counts occurence of character(or words) in that string
print(str.count("i"))


# string.capitalize() -- Capitlize first charcter of your string
str = "this is all lowercase string"
print(str.capitalize())


# string.find("word") -- give position of first occurence of that character/word in string
print(str.find("is"))


# string.replace(oldword, newword) -- replace all occurence of oldwords with newwords
print(str.replace("i", "0"))

