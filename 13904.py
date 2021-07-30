# 과제
import sys
input = sys.stdin.readline
N = int(input())
assign = []
day = 0
for _ in range(N):
    d,w = map(int,input().split())
    assign.append([d,w])
    day = max(day,d)
assign.sort(key = lambda x:x[1],reverse = True) # 높은 점수 순으로

answer = [0 for _ in range(day)]
for i in range(N):
    for j in range(assign[i][0]-1,-1,-1):
        if answer[j] == 0:
            answer[j] = assign[i][1]
            break
print(sum(answer))