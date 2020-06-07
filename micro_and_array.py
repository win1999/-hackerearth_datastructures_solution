t=int(input())
for _ in range(0,t): 
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    z=k-min(arr)
    if(z<0):
        print("0")
    else:
        print(z)
