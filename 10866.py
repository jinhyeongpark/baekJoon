import sys
from collections import deque 

input = sys.stdin.readline

deq = deque()

#push_front X: 정수 X를 덱의 앞에 넣는다.
#push_back X: 정수 X를 덱의 뒤에 넣는다.
#pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 덱에 들어있는 정수의 개수를 출력한다.
#empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
#front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

for _ in range(int(input())):
    comm = input().split()

    if comm[0] == 'push_front':
        deq.appendleft(comm[1])
    elif comm[0] == 'push_back':
        deq.append(comm[1])
    elif comm[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif comm[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(deq))
    elif comm[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif comm[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)