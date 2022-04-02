# Append is little different from write. It doesn't overwrite pre-written content in file. It just append to existing data
# To append, we open file in append mode and then write()

f = open('sampletoappend.txt', 'a')
txt = f.write("Just random text inserted with append")
print(txt)

f.close()