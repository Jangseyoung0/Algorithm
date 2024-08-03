from collections import deque
def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                if j!=i:
                    graph[i].append(j)
    visited=[0]*n
    def bfs(i):
        q=deque([i])    
        visited[i]=1
        while q:
            c=q.popleft()
            for n in graph[c]:
                if visited[n]==0:
                    visited[n]=1
                    q.append(n)
        return 1
    for i in range(n):
        if visited[i]==0:
            answer+=bfs(i)
                
    return answer