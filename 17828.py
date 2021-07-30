# 문자열 화폐
import sys
N,X = map(int,sys.stdin.readline().split())
if N>X or N*26 < X:
    print("!")
    exit()
if N == X:
    print('A'*N)
    exit()
z = X//26
while (N-z)+26*z >= X and X>=26:
    z-=1
sub = 'Z'*z
if X == (N-z)+26*z:
    print('A'*(N-z)+'Z'*z)
else:
    print('A'*(N-z-1)+chr(X-z*26-(N-1-z)+64)+'Z'*z)