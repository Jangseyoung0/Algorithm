from collections import deque
def solution(begin, target, words):
    answer = 0
    words.append(begin)
    visited=[0]*len(words)
    def bfs(begin):
        q=deque([begin])
        while q:
            c=q.popleft()
            if c==target:
                return visited[words.index(c)]
            for i in words:
                change=0
                for j in range(len(begin)):
                    if i[j]!=c[j]:
                        change+=1
                if change==1 and visited[words.index(i)]==0:
                    visited[words.index(i)]=visited[words.index(c)]+1
                    q.append(i)
        return 0
    answer=bfs(begin)      
    return answer