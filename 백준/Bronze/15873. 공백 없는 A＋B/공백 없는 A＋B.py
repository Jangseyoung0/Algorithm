n=list(str(input()))
num=0
for i in range(len(n)):
    if i<len(n)-1 and n[i]=='1' and n[i+1]=='0':
        num+=10
    else:
        num+=int(n[i])
print(num)