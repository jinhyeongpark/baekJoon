T = int(input()) #케이스 개수
Q, D, N, P  = 25, 10, 5, 1
for i in range(T):
    money = int(input())
    res = []
    res.append(str(money // Q))
    money %= Q
    res.append(str(money // D))
    money %= D
    res.append(str(money // N))
    money %= N
    res.append(str(money // P))
    money %= P
    print(" ".join(res))