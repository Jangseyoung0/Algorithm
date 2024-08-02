def solution(n, lost, reserve):
    answer = 0
    a=0
    for i in lost:
        if i in reserve:
            a+=1
            lost[lost.index(i)]=-1
            reserve[reserve.index(i)]=-1
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        if lost[i]!=-1:
            if lost[i]-1 in reserve:
                a+=1
                reserve[reserve.index(lost[i]-1)]=-1
            elif lost[i]+1 in reserve:
                a+=1
                reserve[reserve.index(lost[i]+1)]=-1
    answer=n-(len(lost)-a)
    return answer