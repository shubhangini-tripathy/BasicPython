N = int(input())
A = [int(x) for x in input().split()]
B = int(input())
S = set(A)
count = 0
for i in range(B):
    C = [int(x) for x in input().split()]
    if len(S- set(C))== 0:
        count += 1
print(count)

    
    

    
