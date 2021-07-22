# 서강근육맨
import sys
input = sys.stdin.readline
n = int(input())
muscle = list(map(int,input().split()))
muscle.sort()
if n%2 == 1:
    hap = 0
    for i in range((n-1)//2):
        hap = max(hap,muscle[i]+muscle[-i-2])
    print(max(hap,muscle[-1]))
else:
    hap = 0
    for i in range(n//2):
        hap = max(hap,muscle[i]+muscle[-i-1])
    print(hap)