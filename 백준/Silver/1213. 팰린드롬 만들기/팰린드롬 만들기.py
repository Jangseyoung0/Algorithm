import sys
word=sys.stdin.readline().rstrip()
chars=dict()
for i in word:
    if chars.get(i,0)==0:
        chars[i]=1
    else:
        chars[i]+=1
keys=sorted(chars.keys())
oddc=''
for key in keys:
    if chars.get(key)%2==1:
        if oddc=='':
            oddc=key
        else:
            print("I'm Sorry Hansoo")
            exit()
ans=''
half=''
for key in keys:
    count=chars[key]//2
    half+=key*count
    chars[key]=int(chars[key]/2)
ans+=half
if oddc!='':
    ans+=oddc
ans+=half[::-1]
print(ans)