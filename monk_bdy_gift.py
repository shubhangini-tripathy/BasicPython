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

    

# a = [1,2,3,4,5]
# b = [1,2,3,4,6]
# for i in range(len(b)):
#     if b[i] in a:
#         print("True")
    

    
