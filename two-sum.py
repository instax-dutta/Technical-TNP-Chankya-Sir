arr=list(map(int,input().split()))
target=int(input())
arr.sort()
l=0
r=len(arr)-1
while(l<r):
    x=arr[l]+arr[r]
    if (x==target):
        print(l+1,r+1)
        break
    elif(x>target):
        r-=1
    else:
        l+=1
else:
    print(-1)

