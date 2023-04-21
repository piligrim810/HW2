print("Enter len of array:")
len = int(input())

print("Enter array:")
arr = [int(x) for x in input().split()]

print("Enter target X")
x = int(input())

count = 0
for i in arr:
    if i == x:
        count += 1

print(count)
