#10진수 N -> B진법 출력
N, B = map(int, input().split())#60466175 36
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])