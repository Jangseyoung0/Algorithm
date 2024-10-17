from collections import deque
def solution(n, computers):
    answer = 0
    arr=[[]for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1:
                arr[i].append(j)
                arr[j].append(i)
    def bfs(v,visited,arr):
        q=deque()
        if v not in visited:
            visited.append(v)
            q.append(v)
        while q:
            target=q.popleft()
            for i in arr[target]:
                if i not in visited:
                    q.append(i)
                    visited.append(i)
        return visited
    visited=[]
    for i in range(n):
        if i not in visited:
            visited=bfs(i,visited,arr)
            answer+=1
    return answer