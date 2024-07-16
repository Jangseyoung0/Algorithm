def solution(arr):
    answer = arr[:]
    n=len(arr)
    l=1
    while l<n:
        l*=2
    if n<l:
        for i in range(l-n):
            answer.append(0)
    
    return answer
