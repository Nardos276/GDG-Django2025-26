number=[25, 32, 57, 2, 10]
max=number[0]
for i in range (len(number)):
    if number[i] > max:
        max=number[i]
print("maximum= ", max)