N = int(input())
petrol_capacity = []
min_count = float('inf')
for i in range(N):
    dist, petrol = map(int, input().split())
    petrol_capacity.append((petrol, dist))
petrol_capacity.sort(reverse=True)
distance, petrol = map(int, input().split())
count = 0


def get_min_count(distance, petrol):
    count = 0
    while True:
        for item in petrol_capacity:
            if petrol >= distance:
                return count
            pet, dist = item
            if dist <= distance:
                petrol += pet
                count += 1


print(get_min_count(distance, petrol))
