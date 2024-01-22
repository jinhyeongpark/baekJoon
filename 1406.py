#커서의 개념을 바꿈
#커서를 기준으로 리스트를 둘로 나누어 append와 pop으로 양끝 제어
import sys
from collections import deque 

input = sys.stdin.readline

l1 = deque(input().strip())
l2 = deque()

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if l1:
            l2.appendleft(l1.pop())
    elif command[0] == 'D':
        if l2:
            l1.append(l2.popleft())
    elif command[0] == 'B':
        if l1:
            l1.pop()
    else:
        l1.append(command[1])

l1.extend(l2)
print("".join(list(l1)))