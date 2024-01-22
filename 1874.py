#스택에 push하는 순서는 반드시 오름차순
import sys

input = sys.stdin.readline

n = int(input()) #입력될 숫자의 수
arr = [int(input()) for _ in range(n)] #n개의 숫자들을 arr리스트에 저장

num_stack, res, add, flag = [], [], 1, True

for num in arr: #arr리스트에서 숫자들 하나씩 가져옴
    while add <= num: 
        num_stack.append(add)
        res.append("+")
        add += 1
        
    if num == num_stack[-1]:
        num_stack.pop()
        res.append("-")
    else:
        flag = False
        break
if flag == True:
    for _ in res:
        print(_)
else:
    print("NO")