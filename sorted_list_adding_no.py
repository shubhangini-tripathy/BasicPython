N = int(input())
arr = [int(x) for x in input().split()]
moves = 0
for i in range(len(arr) - 1):
    if arr[i + 1] <= arr[i]:
        moves += arr[i] - arr[i + 1] + 1
        arr[i + 1] = arr[i] + 1
print(moves)
