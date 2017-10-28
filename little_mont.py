N = int(input())
A = [int(x) for x in input().split()]
B = []
length = 0
max_len = 0
for i in range(len(A)):
    if A[i] > 0:
        B.append(A[i])
    else:
        if len(B) > 0 and B[-1] == -(A[i]):
            length += 2
            B.pop(-1)
        else:
            length = 0
            B = []
        if length > max_len:
            max_len = length
print(max_len)
