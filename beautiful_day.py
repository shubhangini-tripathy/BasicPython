N = int(input())
M = [int(x) for x in input().split()]
i, j, sum_forward, sum_backward = 0, N - 1, 0, 0

while i <= j:
    if sum_forward < sum_backward:
        sum_forward += M[i]
        i += 1
    else:
        sum_backward += M[j]
        j -= 1
print(sum_forward * sum_backward)
