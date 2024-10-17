def solution(progresses, speeds):
    answer = []
    left=[]
    for i in range(len(progresses)):
        day=(100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            day+=1
        left.append(day)
    i=0
    while i<len(left):
        j=i
        while j<len(left) and left[j]<=left[i]:
            j+=1
        answer.append(j-i)
        i=j
    return answer