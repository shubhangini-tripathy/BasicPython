n = int(input())
result = []
for i in range(n):
    arr = (input().split())
    name, marks = arr[0], int(arr[1])
    result.append((marks, name))
result.sort(reverse = True)
for x in range(3):
    marks, name = result[x]
    print(name)
