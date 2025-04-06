r=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
total_food=r*unit
res=0
count=0
for i in range(len(arr)):
    if total_food>res:
        res+=arr[i]
        count+=1
    else:
        break
print(count)        
