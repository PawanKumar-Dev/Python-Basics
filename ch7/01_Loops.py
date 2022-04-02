# Loops are way to iterate through content that need to be repeated and how
# There are primarly two loops:

# while loop
fruits = ["Banana", "Apple", "Grapes", "WaterMelon", "Mangoes"]

i = 0  # While counter intialized
while(i < len(fruits)):  # Condition till loop will run
  print(fruits[i])
  i = i+1   # increasing counter



# For loop ---It's easier for looping through sequence like Lists, Tuples or string
for items in fruits:
  print(items)