K, N = map(int, input().split())
arr = [int(x) for x in input().split()]
skill_dict = {}


# def get_max_skill(x, y, z, prev_sum_temp=0):
#     i, j, k, prev_sum1 = x, y, z, prev_sum_temp
#     while k > 0 and min(i, j) >= 0 and max(i, j) < len(arr):
#         i, j, k, prev_sum1 = i + 1, j, k - 1, prev_sum1 + arr[i]

#     i, j, k, prev_sum2 = x, y, z, prev_sum_temp
#     while k > 0 and min(i, j) >= 0 and max(i, j) < len(arr):
#         i, j, k, prev_sum2 = i, j - 1, k - 1, prev_sum2 + arr[j]
#     return max(prev_sum1, prev_sum2)

# print(get_max_skill(0, len(arr) - 1, K, 0))


# K, N = map(int, input().split())
# arr = [int(x) for x in input().split()]
# skill_dict = {}


def get_max_skill(arr, i, j, k, prev_sum=0):
    if k <= 0:
        return prev_sum
    if min(i, j) < 0 or max(i, j) >= len(arr):
        return prev_sum
    # if (i + 1, j, k - 1) not in skill_dict:
    #     skill_dict[(i + 1, j, k - 1)] = get_max_skill(arr, i + 1, j, k - 1)
    # if (i, j - 1, k - 1) not in skill_dict:
    #     skill_dict[(i, j - 1, k - 1)] = get_max_skill(arr, i, j - 1, k - 1)

    return max(get_max_skill(arr, i + 1, j, k - 1, prev_sum + arr[i]),
               get_max_skill(arr, i, j - 1, k - 1, prev_sum + arr[j]))


print(get_max_skill(arr, 0, len(arr) - 1, K, 0))
