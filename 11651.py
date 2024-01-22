import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
newNums = sorted(nums, key = lambda x:(x[1],x[0]))
for x,y in newNums:
    print(x, y)
