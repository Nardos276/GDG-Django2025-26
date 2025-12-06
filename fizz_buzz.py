num=int(input("Enter a number: "))
def fizz_buzz(num):
    ans= []
    for i in range (1,num+1):
        if i%3==0:
            ans.append("Fizz")
            continue
        elif i%5==0:
            ans.append("Buzz")
            continue
        elif i%3==0 and i%5==0:
            ans.append("FizzBuzz")
            continue
        else:
            ans.append(f"{i}")
    return ans
print(fizz_buzz(num))

   
