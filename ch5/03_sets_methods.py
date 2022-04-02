# Sets Methods
# set.add() -- can add value inside a set but only non-repetive
a = set()
a.add(5)
a.add(6)
a.add(7)

print(a)


# We cannot add mutable data type into sets such as Dict, List
# we can add tuples easily since its immutable
a.add((1, 2, 3))
print(a)


# len(set) -- Prints length of a set
print(len(a))


# set.remove(elment) -- Removes the element from set
a.remove(7)
print(a)


# set.pop(element) -- Randomly remove and give tht element
print(a.pop())
print(a)

# set.clear() -- empty out the set
a.clear()
print(a)


# set.union() -- return union of two sets (it return full elements of both sets)
# set.intersect() -- return the interect of two sets (only returnt the elements that are common in both sets)