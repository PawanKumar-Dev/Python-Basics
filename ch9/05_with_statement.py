# with statement is best way to open files, since it close file automatically

with open('sample.txt', 'r') as f:
  print(f.read())