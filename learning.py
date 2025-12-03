"""x = int(input ("number: " ))
if x > 0:
    print (f"{x} is positive")
elif x < 0:
    print (f"{x} is negattive")
else:
    print (f"{x} is zero")"""
x = int(input ("num1: "))
y = int(input ("num2: "))
print ("choose operator:")
print (" 1: Addition ")
print ("2: Subtraction ")
print ("3: Multiplication ")
print ("4: Division ")
print ("5: Modulus ")
z= int(input ("Operation: "))
if z == 1:
    result = x + y
    print (f"{x} + {y} is {result}")
elif z == 2:
    print (f"{x} + {y} is {x-y}")
elif z == 3:
    print (f"{x} + {y} is {x*y}")
elif z == 4:
    print (f"{x} + {y} is {x/y}")
elif z == 5:
    print (f"{x} + {y} is {x%y}")


