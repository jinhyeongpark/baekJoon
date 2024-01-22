import sys
from collections import deque 

input = sys.stdin.readline

arr = deque()

for _ in range(int(input())):
    comm = list(input().split())

    if comm[0] == 'push':
        arr.append(comm[1])

    elif comm[0] == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)

    elif comm[0] == 'size':
        print(len(arr))

    elif comm[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif comm[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    else:
        if arr:
            print(arr[-1])
        else:
            print(-1)