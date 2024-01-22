import sys          
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
new_nums = [(y,x)for x,y in list(enumerate(sorted(list(set(nums)))))]
num_dict = dict(new_nums)
for num in nums:
    print(num_dict[num], end=" ")