def gcd(n,m):

    for i in range(1,min(m,n)+1):
        if n%i==0 and m%i==0 :
            num=i
        
    return num
print(gcd(12,144))
