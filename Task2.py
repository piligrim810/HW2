print("Enter array:")

arr = [int(x) for x in input().split()]

print("Enter target X:")
x = int(input())

closeOne = arr[0]
diff = abs(x - int(arr[0]))


for i in arr:
    if abs(x - int(i)) < diff:
        closeOne = i
        diff = abs(x - int(i))

print(closeOne)
