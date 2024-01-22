#100x100의 2차원 배열 생성
arr = [[0 for _ in range(100)] for _ in range(100)]
#색종이 수를 입력받음
rep = int(input())
for i in range(rep):
    x, y = map(int,input().split())
    #색종이 좌측 하단 모서리의 x, y 좌표를 받음
    x-=1
    y-=1
    for j in range(10):
        for h in range(10):
            arr[y+h][x+j] = 1

target_number = 1
count = 0

# 중첩된 루프를 사용하여 특정 숫자를 카운트
for row in arr:
    for number in row:
        if number == target_number:
            count += 1
print(count)
    