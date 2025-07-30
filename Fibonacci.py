lis=[0,1]
series_len=int(input("Enter how many numbers you want in the series : "))
first_num=lis[0]
next_num=lis[first_num+1]
while len(lis)<series_len:
    a=first_num+next_num
    lis.append(a)
    first_num=next_num
    next_num=a
print('Your Fibonacci series is :\n')
print(lis)

