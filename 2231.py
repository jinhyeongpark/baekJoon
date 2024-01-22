N = int(input())
numList = list(range(1,N+1))
res= 0

for num in numList:
    digit_sum = sum([int(digit) for digit in str(num)])  # 각 자릿수의 합을 계산합니다.
    if num + digit_sum == N:
        res = num
        break
print(res)