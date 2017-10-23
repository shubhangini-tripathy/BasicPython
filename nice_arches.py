M = int(input())
count = 0
for i in range(M):
    F = input()
    N = []
    for j in F:
        if len(N) > 0 and j == N[-1]:
            N.pop(-1)
        else:
            N.append(j)
    if len(N) == 0:
        count += 1
print(count)
