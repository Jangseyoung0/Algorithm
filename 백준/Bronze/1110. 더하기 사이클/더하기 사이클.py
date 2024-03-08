import sys
n=int(sys.stdin.readline())
arr=[]
arr.append(n//10)
arr.append(n%10)
c=0
while True:    
    arr.append((arr[-1]+arr[-2])%10)
    c+=1 
    if arr[-2]==arr[0] and arr[-1]==arr[1]:
        break
   
print(c)