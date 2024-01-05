from collections import Counter
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer=''
    p=Counter(participant)
    c=Counter(completion)
    p.subtract(c)
    for key,num in p.items():
        if num >0:
            answer=key
    
    return answer