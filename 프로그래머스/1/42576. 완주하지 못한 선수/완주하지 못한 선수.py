def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        if p in dict:
            dict[p]+=1
        else:
            dict[p]=1
    for p in completion:
        if p in dict:
            dict[p]-=1
    for i in dict:
        if dict[i]==1:
            answer=i
    return answer