x=int(input())
for i in range(0,x):
    y=int(input())
    ls=[int(x) for x in input().split()]
    z=min(ls)
    a=ls.count(z)
    if(a%2==0):
        print("Unlucky")
    else:
        print("Lucky")
