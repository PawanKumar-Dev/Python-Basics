# Just like break, continue is used for manipulation of loop
# When "continue" condition is met, we skip that iteration

for item in range(5):
  if(item == 2):
    continue   # Will allow us to skip iteration 2
  print(item)