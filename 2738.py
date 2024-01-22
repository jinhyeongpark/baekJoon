# A = []
# B = []

# N, M = map(int,input().split())

# for i in range(N):
#     A.append(list(map(int, input().split())))

# for i in range(N):
#     B.append(list(map(int, input().split())))

# for i in range(N):
#     for j in range(M):
#         print(A[i][j]+B[i][j], end=" ")
#     print()
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = [[A[i][j] + B[i][j] for j in range(M)]for i in range(N)]

for row in result:
    print(*row)