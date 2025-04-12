n = int(input())
m = int(input())

def differenceOfSum(n,m):
    res1=0
    res2=0
    if n>0 and m>0:
        for i in range(1,m+1):
            if i%n==0:
                res1+=i
            else:
                res2+=i
        return (res2-res1)
  
  

print(differenceOfSum(n,m))
