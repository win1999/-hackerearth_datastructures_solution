x=int(input())
for i in range(x):
    s=int(input())
    ar=list(map(int,input().split()))
    if(sum(ar)-max(ar)>max(ar)):
        print("Yes")
    else:
        print("No")
