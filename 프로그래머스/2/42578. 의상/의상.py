def solution(clothes):
    answer=1
    clothdict={}
    for item,cate in clothes:
        if cate not in clothdict:
            clothdict[cate]=[item]
        else:
            clothdict[cate].append(item)
    for item in clothdict:
        answer*=(len(clothdict[item])+1)
    
    answer-=1
    
    return answer