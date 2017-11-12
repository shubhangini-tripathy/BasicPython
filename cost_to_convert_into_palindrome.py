def is_palindrom(S):
    i = 0
    result = True
    while i < len(S):
        if (S[i] != S[-(i + 1)]):
            result = False
            return result
        i = i + 1
    return result


def get_min_cost(S):
    i = 0
    cost = 0
    while i < len(S) // 2:
        if S[i] != S[-i - 1]:
            cost += ord(min(S[i], S[-i - 1])) - 96
        i += 1


T = int(input())
for t in range(T):
    S = input()
    if is_palindrom(S):
        print(0)
    else:
