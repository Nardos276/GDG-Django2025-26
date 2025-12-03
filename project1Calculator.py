num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
def addition(num1, num2):
    return num1+num2
def substraction(num1, num2):
    return num1-num2
def multiplication(num1, num2):
    return num1*num2
def division(num1, num2):
    return num1/num2
#print("Choose operation: ")
#print(" 1. Addition(+)\n 2. Substration(-)\n 3.Multiplication(*)\n 4.Division(/) ")
operation= input("Choose operation(+, -, *, /)")
if operation=="+":
    #result= addition(num1, num2)
    print(addition(num1, num2))
elif operation=="-":
    #result= substraction(num1, num2)
    print(substraction(num1, num2))
elif operation=="*":
    #result= multiplication(num1, num2)
    print(multiplication(num1, num2))
elif operation=="/":
    #result= division(num1, num2)
    print(division(num1, num2))
else:
    print("Invalid Input")
    


