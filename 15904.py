# UCPC는 무엇의 약자일까?
import sys
line = sys.stdin.readline()
ucpc = ['U','C','P','C']
for x in ucpc:
    if x in line:
        idx = line.index(x)
        line = line[idx+1:]
    else:
        print("I hate UCPC")
        exit()
print("I love UCPC")