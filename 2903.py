N = int(input())
num = 2
for i in range(N):
    res = num +(num-1)
    num = res
print(res**2)