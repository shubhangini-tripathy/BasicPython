def is_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in range(2,  N + 1):
    if is_prime(num) == True:
        print(num,end= ' ')
