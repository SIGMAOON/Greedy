# 모두의 마블
import sys
input = sys.stdin.readline
n = int(input())
level = list(map(int,input().split()))
print(max(level)*(n-2)+sum(level))