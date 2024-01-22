import sys
from collections import deque 
input = sys.stdin.readline
deq = deque()

N = int(input())

for _ in range(N):
    get = input().split()
    if get[0] == 'push':
        deq.append(get[1])
    elif get[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif get[0] == 'size':
        print(len(deq))
    elif get[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif get[0] == 'top':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])