import sys
k=int(sys.stdin.readline())
for i in range(k):
    score=list(map(int,sys.stdin.readline().split()))
    score.remove(score[0])
    score.sort()
    diff=[]
    for j in range(len(score)-1):
        diff.append(score[j+1]-score[j])
    print('Class',i+1)
    print('Max ',score[-1],',',' Min ',score[0],',',' Largest gap ',max(diff),sep='')
