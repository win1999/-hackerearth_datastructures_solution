import numpy as np
x=int(input())
arr=[int(y) for y in input().split()]
arr1=[int(y) for y in input().split()]
z=(np.add(arr,arr1))
for ele in z:
    print(ele,end=" ")
