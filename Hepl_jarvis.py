n=int(input())
for _ in range(n):
    a=list(map(int,list(input())))
    x=[]
    for i in range(min(a),max(a)+1):
        x.append(i)
    if len(set(x)-set(a))==0 and len(set(a))==len(a):
        print('YES')
    else:
        print('NO')
