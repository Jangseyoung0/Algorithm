import sys
word=sys.stdin.readline().rstrip()
result=[]
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        f=''.join(reversed(word[:i]))
        s=''.join(reversed(word[i:j]))
        t=''.join(reversed(word[j:]))
        result.append(f+s+t)
print(sorted(result)[0])