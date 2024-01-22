from itertools import*

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr_combinations = list(combinations(arr,3))
arr_res = [sum(nums) for nums in arr_combinations]
res = [num for num in arr_res if num <= M]
print(max(res))