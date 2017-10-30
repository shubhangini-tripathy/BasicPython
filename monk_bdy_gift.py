a, b, c = map(int, input().split())
temp = a
while abs(temp) <= 109:
    if temp == b:
        break
    temp += c

if abs(temp) <= 109:
    print("Yes")
else:
    print("No")
