N , M = list(map(int, input().split())) #바구니 수와 시도할 수를 입력받음

basket = [0] * N #M개의 빈 바구니 생성

for i in range(M): #N번의 시도 시작
    start, end, num = list(map(int, input().split())) #바구니 범위와 숫자공을 받음
    basket[start-1:end] = [num] * (end - start + 1) #해당 범위에 슬라이싱을 통해 숫자공을 넣음

for i in basket: #출력
    print(i,end = " ")
