nums=[]
n=int(input("How many numbers do you want in the array:" ))
for i in range(n):
    nums.append(int(input("Enter the numbers: ")))
for j in range (len(nums)):
    for i in range(len(nums)-1):
        if nums[i]==0:
            temp=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=temp
        else:
            continue
print("Output: ", nums)