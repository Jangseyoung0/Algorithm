import sys
import itertools
n=int(sys.stdin.readline())
numli=[i for i in range(1,n+1)]
npr=list(itertools.permutations(numli,n))
for i in range(len(npr)):
    print(*npr[i])