n= int(input())
m = n
sum1 = 0
while m :
    sum1 += m%10
    m //= 10
s = str(sum1)
print(s)
if (s==s[::-1]) :
    print('YES')
else :
    print('NO')
