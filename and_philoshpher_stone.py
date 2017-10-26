N = int(input())
C = [int(x) for x in input().split()]
m, n = map(int, input().split())
D = []
possible = False
for j in range(m):
    T = input()
    if T == "Harry":
        D.append(C.pop(0))
    else:
        if len(D) > 0:
            D.pop(-1)
    if sum(D) == n:
        possible = True
        break

if possible:
    print(len(D))
else:
    print(-1)
