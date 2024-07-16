def solution(arr, k):
    answer = []
    cnt=0
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            cnt+=1
    if cnt<k:
        for i in range(k-cnt):
            answer.append(-1)
    else:
        answer=answer[:k]
        
    return answer