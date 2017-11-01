N = int(input())
for j in range(N):
    P = int(input())
    A = set([int(x) for x in input().split()])
    S = int(input())
    for i in range(S):
        Y = int(input())
        if Y in A:
            print("Yes")
        else:
            print("No")
