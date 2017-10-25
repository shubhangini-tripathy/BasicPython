t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    c = [int(x) for x in input().split()]
    for j in range(n):
        d = list(c)
        for k in range(len(c)):
            if k == 0:
                if c[k + 1] == 1:
                    d[k] = 1
                else:
                    d[k] = 0
            elif k == len(c) - 1:
                if c[k - 1] == 1:
                    d[k] = 1
                else:
                    d[k] = 0
            else:
                if c[k + 1] == 1 and c[k - 1] == 1:
                    d[k] = 1
                else:
                    d[k] = 0
        c = d
    print(' '.join([str(x) for x in c]))
