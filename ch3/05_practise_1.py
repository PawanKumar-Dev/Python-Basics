# Function giving good afternoon
a = input("Enter your name plz! ")
b = ", Good Afternoon"
print(a + b)


# Write a simple template (1st way)
a = input("Write your name! ")
b = input("Enter today's date! ")

letter = '''Dear ''' + a + ''',
          You are selected! \n''' + b
print(letter)



# Write a simple template (2nd way)
a = input("Write your name! ")
b = input("Enter today's date! ")

letter = ''' Dear <|NAME|>,
          You are selected!
          <|DATE|> '''
letter = letter.replace("<|NAME|>", a)
letter = letter.replace("<|DATE|>", b)
print(letter)