B = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = 15
for i in range(len(B)):
    for j in range(i + 1, len(B)):
        if B[i] + B[j] == A:
            print(i, j)
