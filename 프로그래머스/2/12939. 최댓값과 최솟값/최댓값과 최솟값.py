def solution(s):
    answer = ''
    sint=list(map(int, s.split()))
    answer+=str(min(sint))
    answer+=' '
    answer+=str(max(sint))
    return answer
