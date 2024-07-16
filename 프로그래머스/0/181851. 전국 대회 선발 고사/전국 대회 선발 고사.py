def solution(rank, attendance):
    answer = 0
    dict={}
    cnt=0
    for i in range(1,len(rank)+1):
        if attendance[rank.index(i)]==1:
            dict[rank.index(i)]=attendance[rank.index(i)]
    print(dict)
    dict=list(dict.keys())
    for i in range(3):
        answer=answer*100+dict[i]
    return answer