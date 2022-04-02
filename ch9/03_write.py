# First, we must open file in 'w' mode.
# Then, use the write() method to write file. It takes the content as argument
# If the file doesn't exist, Py will create one and write it

f = open('samplewrite.txt', 'w')
txt = f.write("Writing content to file")
print(txt)

f.close()