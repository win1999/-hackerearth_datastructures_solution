
t=int(input())
for i in range(0,t):
    l=int(input())
    arr=[int(x) for x in input().split()]
    for i in arr:
        z=arr.count(i)
        if(z==1):
            print(i)
        
                
