def factor(n):
    lis=[]
    for i in range(1,n+1):
        if n%i==0:
            lis.append(i)
        
    return lis    
        
def gcd(n,m):
    lis1=factor(n)
    lis2=factor(m)
    lis3=[]
    for i in range(len(lis1)-1):
        if lis1[i]  in lis2:
            lis3.append(lis1[i])
    return lis3[-1]
    
print(gcd(12,8))
