n=int(input())
arr=list(map(int,input().split()))
arr.sort()
e,o=[],[]
for i in range(len(arr)):
    if arr[i]==0:
        continue
    else:
        e.append(arr[i]) if i%2==0 else o.append(arr[i])
print(e[1]+o[1])
