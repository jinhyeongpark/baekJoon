import sys

input = sys.stdin.readline

N= int(input())

datas = [input().strip() for _ in range(N)]

for data in datas:
    while "()" in data:
        data = data.replace("()", "")
    if len(data) == 0:
        print("YES")
    else:
        print("NO")