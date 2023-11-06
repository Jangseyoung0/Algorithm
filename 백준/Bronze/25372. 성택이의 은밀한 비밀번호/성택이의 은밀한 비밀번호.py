import sys
n=int(sys.stdin.readline())
for _ in range(n):
    password=sys.stdin.readline().strip()
    if len(password)<6 or len(password)>9:
        print("no")
    else:
        print("yes")