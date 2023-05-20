def changetype(choosenvariable, changein):
  changein=changein
  choosen={
    1:int(choosenvariable),
    2:float(choosenvariable),
    3:str(choosenvariable)
  }
  return choosen.get(changein)




x=10
y="Hello"
z=10.56

#print the question
print(f'1. {x} is {type(x)}\n2. {y} is {type(y)}\n3. {z} is {type(z)}')
choosenvariable=input('\nchange data type: ')

#Reference to the variables
if choosenvariable=='1':
  choosenvariable=x
elif choosenvariable=='2':
  choosenvariable=y
elif choosenvariable=='3':
  choosenvariable=z

#print question 2
changein=input('\nchange datatype in\n\n1. inteterger\n2. float\n3. string\nchose a number: ')
print(changetype(choosenvariable, int(changein)))



    
