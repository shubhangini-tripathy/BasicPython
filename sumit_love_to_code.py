from fractions import gcd
t = int(input())
for i in range(t):
    count = 0
    n, a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    count = n // a
    if b % a != 0:
        count = count + (n // b) - (n * gcd(a, b) // (a * b))
    if c % a != 0 and c % b != 0:
        count = count + (n // c) - (n * gcd(a, c) // (a * c)) - (n * gcd(b, c) // (b * c))
    print(count)
