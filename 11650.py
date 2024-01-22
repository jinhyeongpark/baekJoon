N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
newNums = sorted(nums)
for x,y in newNums:
    print(x, y)