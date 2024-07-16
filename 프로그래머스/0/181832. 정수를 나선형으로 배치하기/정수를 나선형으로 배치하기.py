def solution(n):
    answer = [[0]*n for _ in range(n)]
    s=0
    e=n
    num=0
    while num<n**2:   
        for i in range(s,e):
            num+=1
            answer[s][i]=num
        for i in range(s+1,e):
            num+=1
            answer[i][e-1]=num
        for i in range(e-2,s-1,-1):
            num+=1
            answer[e-1][i]=num
        for i in range(e-2,s,-1):
            num+=1
            answer[i][s]=num
        s+=1
        e-=1       
    return answer