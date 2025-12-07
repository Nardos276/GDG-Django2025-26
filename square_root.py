x = int(input("Enter a non-negative integer: "))

if x < 0:
    print("Invalid input: must be non-negative.")
else:
    ans = 0
    for i in range(x + 1):
        if i * i <= x:
            ans = i
        else:
            break
    print("Output:", ans)
