A = int(input())
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
count = 0
while len(B) > 0:
    if B[0] != C[0]:
        B.append(B.pop(0))
    else:
        B.pop(0)
        C.pop(0)
    count += 1
print(count)
