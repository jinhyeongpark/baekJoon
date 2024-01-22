N, M = map(int, input().split())
MNboard = [input() for _ in range(N)]
#print(MNboard)
listForlist= []
listForMinNum = []

for i in range(N-7):
    for j in range(M-7):
        mnboard = [line[j:j+8] for line in MNboard[i:i+8]]
        listForlist.append(mnboard)

for sentences in listForlist: #보드판을 자르는 모든 경우의 수를 담아서 하나씩 꺼냄
    W = 'W'
    B = 'B'
    count = 0
    for _ in range(2):
        if _ == 0:
            if sentences[0][0] == W: #W로 시작하는 경우 WBWBWBWB로 확인을 시작
                pass
            else:
                W, B = B, W   
        else: #W로 시작하더라도 BWBWBWBW로 확인하는게 더 유리할 경우를 생각
            if sentences[0][0] == B: #W로 시작하는 경우
                pass
            else:
                W, B = B, W
        for i in range(8): #8개의 행에 대해 검사
            if i % 2 == 0: #짝수 번째 행의 경우
                for j in range(8):
                    if j % 2 == 0: #짝수 번째 열의 경우
                        if sentences[i][j] != W:
                            count += 1
                    else: #홀수 번째 열의 경우
                        if sentences[i][j] != B:
                            count += 1
            else: #홀수 번째 행의 경우
                for j in range(8):
                    if j % 2 == 0:
                        if sentences[i][j] != B:
                            count += 1
                    else:
                        if sentences[i][j] != W:
                            count += 1   
        listForMinNum.append(count)
        count = 0
    
print(min(listForMinNum))