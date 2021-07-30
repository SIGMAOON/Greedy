# 걷는 건 귀찮아, 으악
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
p =  list(map(int,input().split()))
x = list(map(int,input().split()))
mx = [p[i]+x[i] for i in range(n)]
if p[-1]+x[-1] < m:
    print(-1)
    exit()
curr = [m]
while curr[-1]!=1:
   for i in range(len(p)-1,-1,-1):
       if mx[i] >= curr[-1]:
           pass
        else:
            curr.append(p[i+1])
            break
    p = p[:p.index(curr[-1])]
print(len(curr)-1)
    