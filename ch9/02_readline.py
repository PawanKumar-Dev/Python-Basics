# readline() reads a line by line content

#reading 1st line
fhandle = open('sample.txt', 'r')
txt = fhandle.readline()
print(txt)

#reading 2nd line
txt = fhandle.readline()
print(txt)

#reading 3rd line
txt = fhandle.readline()
print(txt)

fhandle.close()