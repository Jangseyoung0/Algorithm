import sys
arr=[False,False]+[True]*(1000001-2)
for i in range(2,1001):
        for j in range(i*2,1000001,i):
            if arr[j]==True:
                arr[j]=False

while True:   
    n=int(sys.stdin.readline())
    if n==0:
        break
    flag=0
    for i in range(3,n,2):
        if arr[i] and arr[n-i]:
            print(n,"=",i,"+",n-i)
            flag=1
            break
    if flag==0:
         print("Goldbach's conjecture is wrong.")



