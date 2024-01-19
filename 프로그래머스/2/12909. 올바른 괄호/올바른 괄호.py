def solution(s):
    answer = True
    rc=0
    if s[0]==")":
        answer=False       
    else:
        for i in s:
            if i=="(":
                rc+=1
            else:
                rc-=1
            if rc<0:
                answer=False
    
    if s[-1]=="(" or rc>0:
        answer=False         
    return answer