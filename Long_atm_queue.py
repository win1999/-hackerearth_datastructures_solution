s=int(input())
cns=1
a=list(map(int,input().split()))
for i in range(0,s-1):
    if(a[i]>a[i+1]):
        cns+=1
print(cns)
