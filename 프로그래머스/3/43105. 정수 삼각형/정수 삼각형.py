def solution(triangle):
    n=len(triangle)
    nums=[]
    for i in range(1,n):
        for j in range(0,i+1):            
            if j==0:
                triangle[i][j]=triangle[i][j]+triangle[i-1][j]
            elif j==i:
                triangle[i][j]=triangle[i][j]+triangle[i-1][j-1]
            else:
                triangle[i][j]=max(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j])
    answer = max(triangle[n-1])
    return answer