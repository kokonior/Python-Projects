def prefix_sum(arr,n,a,b):
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]
    return (prefix[b]-prefix[a-1])
            

n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    a,b=map(int,input().split())
    print(prefix_sum(arr,n,a,b))
