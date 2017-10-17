A = int(input())
B = []
for i in range(A):
    C = int(input())
    if C != 0:
        B.append(C)
    else:
         if len(B)>0:
             B.pop(-1)
print(sum(B))

        

        




        
        



    

 