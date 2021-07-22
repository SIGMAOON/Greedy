# 햄버거 분배
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
hp = list(input().strip())
start = end = 0
for i in range(N):
    if hp[i] == 'P':
        if i-K < 0:
            start = 0
        else:
            start = i-K
        if i+K > N-1:
            end = N-1
        else:
            end = i+K
            
        for j in range(start,end+1):
            if hp[j] == 'H':
                hp[j] = 'X'
                break
print(hp.count('X'))