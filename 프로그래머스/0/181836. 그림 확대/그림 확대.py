def solution(picture, k):
    answer=[]
    for i in picture:
        resize=''
        for j in i:
            resize+=j*k
        for l in range(k):
            answer.append(resize)
                
    return answer