# 소가 길을 건너간 이유 3
import sys
input = sys.stdin.readline
N = int(input())
cow = []
for _ in range(N):
    come,check = map(int,input().split())
    cow.append([come,check])
cow.sort()

out = sum(cow[0])

for so in cow[1:]:
    if so[0] >= out:
        out = sum(so)
    else:
        out+=so[1]
print(out)