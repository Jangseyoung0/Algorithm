def solution(genres, plays):
    answer = []
    mdict={}
    for i in range(len(genres)):
        if genres[i] not in mdict:
            mdict[genres[i]]=[plays[i]]
        else:
            mdict[genres[i]].append(plays[i])
    mdict=sorted(mdict.items(), key = lambda x : -sum(x[1]))

    for i in range(len(mdict)):
        mdict[i][1].sort(reverse=True)


    for i in range(len(mdict)):   
        if len((mdict[i][1])) > 1:
            for j in range(2):
                answer.append(plays.index(mdict[i][1][j]))
                plays[plays.index(mdict[i][1][j])]=0
        else:
            answer.append(plays.index(mdict[i][1][0]))
    
    return answer