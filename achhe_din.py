T= int(input())
for i in range(T):
    N= int(input())
    A = [int(x) for x in input().split()]
    for j in range(len(A)):
        if A.count(A[j])==1:
            print(A[j])



        
    