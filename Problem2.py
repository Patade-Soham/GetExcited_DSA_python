def primeproduct(m):
  lis=[]
  for i in range(2,m):
    if m%i==0:
      lis.append(i)
  if len(lis) == 2:
    return True
  else:
    return False
def delchar(s,c):
    s=str(s).replace(c,"",-1)
    return s  

def shuffle(lis1,lis2):
  new_lis=[]
  if len(lis1)>len(lis2):
    bigger_lis=lis1
  elif len(lis2)>len(lis1):
    bigger_lis=lis2
  elif len(lis2)==len(lis1):
    bigger_lis=lis1


  if bigger_lis==lis1:
    for i in range(len(lis2)):
      bigger_lis.insert(2*i+1,lis2[i])
    return bigger_lis
  elif bigger_lis == lis2:
    for i in range(len(lis1)):
      bigger_lis.insert(2*i,lis1[i])
    return bigger_lis
  elif bigger_lis==lis1:
    for i in range(len(lis2)):
      bigger_lis.insert(2*i+1,lis2[i])
    return bigger_lis

print(shuffle([2,4,6,1,7],[8,4,2,7,6,4,4]))

