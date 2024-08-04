def solution(clothes):
    answer = 1
    dict={}
    for i in range(len(clothes)):
        if clothes[i][1] not in dict:
            dict[clothes[i][1]]=1
        else:
            dict[clothes[i][1]]+=1
    for i in dict:
        answer*=(dict[i]+1)
    answer-=1
    return answer