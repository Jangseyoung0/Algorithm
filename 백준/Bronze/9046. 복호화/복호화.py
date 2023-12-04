import sys
n=int(sys.stdin.readline())
for _ in range(n):
    code=sys.stdin.readline().strip()
    code=code.replace(" ", "")
    cnt=[0 for _ in range(26)]
    for i in code:
        cnt[ord(i)-97]+=1
    if cnt.count(max(cnt))>1:
        print("?")
    else:
        print(chr(cnt.index(max(cnt))+97))