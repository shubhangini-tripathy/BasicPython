N = int(input())
for i in range(N):
    S = list(input())
    T = list(input())
    count = 0
    for j in (S):
        if j in T:
            T.remove(j)
        else:
            count += 1
    print(count + len(T))
