# 저울
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
answer = 1
for num in nums:
    if answer < num:
        break
    answer+=num
print(answer)