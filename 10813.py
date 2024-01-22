N , M = list(map(int, input().split()))
basket = []
for i in range(N):
    basket.append(i+1)
for j in range (M):
    a , b = list(map(int, input().split()))
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]
for _ in basket: #출력
    print(_,end = " ")