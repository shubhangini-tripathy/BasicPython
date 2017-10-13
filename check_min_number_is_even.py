for i in range(T):
    C = int(input())
    A = [int(x) for x in input().split()]
    if A.count(min(A))%2 == 0:
        print("Unlucky")
    else:
         print("Lucky")