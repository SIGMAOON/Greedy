# 통나무 건너뛰기
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    gap = 0
    for i in range(N-2):
        gap = max(gap,L[i+2]-L[i])
    print(gap)