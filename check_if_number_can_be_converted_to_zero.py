T = int(input())

A = int(input())
for i in range(1):
    B = [int(x) for x in input().split()]
    if max(B) - min(B) > 0 or min(B) <= A:
        print("NO")
    else:
        print("YES")