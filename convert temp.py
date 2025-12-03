print ("choose a number: ")
print ("1. celsius")
print ("2. fahrenheit")
z =int (input ())
x = int (input ("temp:" ))
if z==1:
    result = 9/5 * x + 32
    print (f"Temperature in fahrenheit is {result}")
elif z==2:
    result = 5/9*(x - 32) 
    print (f"Temperature in celsius is {result}")


