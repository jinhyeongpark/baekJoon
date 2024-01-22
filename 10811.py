N , M = list(map(int, input().split()))
basket = list(range(1,N+1))
for i in range(M):
    start , end = list(map(int, input().split()))
    basket[start-1:end] = basket[start-1:end][::-1]
for _ in basket: #출력
    print(_,end = " ")