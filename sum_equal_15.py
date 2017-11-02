A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
C = 15
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        for k in range(j + 1, len(A)):
            if A[i] + A[j] + A[k] == C:
                print(A[i], A[j], A[k])
