from collections import Counter
def solution(s):
    answer = True
    if s[0]==')' or s[-1]=='(':
        return False
    left=0
    right=0
    for i in range(len(s)):
        if s[i]=='(':
            left+=1
        if s[i]==')':
            right+=1
        if left<right:
            return False
    if left!=right:
        return False
    return True