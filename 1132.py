# 합
import sys
input = sys.stdin.readline
n = int(input())

line = []
ap = [] #맨앞 알파벳
for _ in range(n):
    line.append(list(input().strip()))
for i in range(n):
    ap.append(line[i][0])
line2 = [] #알파벳 종류 구하기
for x in line:
    line2+=list(x)
line2 = list(set(line2))

dic = {} #계수 구하기
for a in line2:
    dic[a] = 0
for st in line:
    for i in range(len(st)):
        dic[st[i]]+=10**(len(st)-i-1)
result = list(dic.items())

result.sort(key = lambda x:x[1],reverse = True) 

if len(result) == 10:
    for i in range(9,-1,-1):
        if result[i][0] not in ap:
            rem = result[i]
            result.remove(rem)
            break

answer = 0
start = 9
for x in result:
    answer+=(start*x[1])
    start-=1
print(answer)