# Files can be read and write in Py
# There are mainly two types of files:
# Text File(.txt etc): they can be simple programs like notepad
# Binary File(.jpg, .dat etc): need special file openers

# Opening File is done with open() function
# 2nd part mode:
# 'r' --> read mode, 'w' --> write mode
# 'a' --> append mode, '+' --> updating mode

# 'rb': readmode for binary files, 'rt': readmode for text file

# In files read is by "default mode".

fhandle = open('sample.txt', 'r')  # open file
txt = fhandle.read()               # read file
print(txt)                         # printing the open file
fhandle.close()                    # close the opened file