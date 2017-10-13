k , l = map(int, input().split())
B = [int(x) for x in input().split()]
ques_count=0
skip_count=0
for i in range (len(B)):
    if B[i]<=l:
        ques_count  += 1
    else:
        skip_count +=1
        if skip_count>1:
            break
print(ques_count)
