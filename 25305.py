from heapq import *

N, k = map(int, input().split())
scores = list(map(int, input().split()))
print(nlargest(k,scores)[-1])