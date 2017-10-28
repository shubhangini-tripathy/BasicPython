s = input()
t = input()
q, x = map(int, input().split())
sets, sett = set(s), set(t)
diff = len(sett.difference(sets)) > 0
for k in range(q):
    if diff:
        print("No")
    else:
        i, j = map(int, input().split())
        i, j = i - 1, j - 1
        u = s[:i] + s[j + 1:]
        if t in u:
            print("Yes")
        else:
            print("No")
