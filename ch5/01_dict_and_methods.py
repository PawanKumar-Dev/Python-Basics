# Dictionary is collection of { "key" : "value" } pair
# It looks pretty similar to JSON and Js Object
# They are unordered. Mutable(you can update them)
# Keys are unique in Dictionary

# Declaring a dict
myDict = {
  "firstname" : "Pawan",
  "lastname": "Kumar",
  "profession" : "Web Dev"
}

print(myDict)

# accessing the type
print(type(myDict))

# accessing the value by key
print(myDict["firstname"])

# accessing all keys of dict
print(myDict.keys())

#similarly we can access values
print(myDict.values())

# access all content of a dict as a list with key:value tuples
print(myDict.items())

# You can update or add new key:value pair in Dictionary too
updateDict = {
  "DOB": 1994
}

myDict.update(updateDict)
print(myDict)


#IMP INTERVIEW QSTN
# get() gives values from dict.
print(myDict.get("firstname2")) # gives us none in return
print(myDict['firstname2']) # throws errors
