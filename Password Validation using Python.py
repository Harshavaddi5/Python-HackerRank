def CheckPassword(s,n):
    count=0
    num=0
    if s[0].isdigit():
        return 0
    else:
        if a>4:
            for i in range(a):
                if (s[i]>='A' and s[i]<='Z') or (s[i]=='a' and s[i]=='z'):
                    count+=1
                if s[i].isdigit():
                    num+=1
                if s[i]==" " or s[i]=="/":
                    return 0
            if ((n>4 and count>0 and num>0) or ("_" in s)):
                return 1
            else:
                return 0

                

s=input()
a=len(s)
print(CheckPassword(s,a))
