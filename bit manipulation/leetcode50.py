x = 2.00
n = -200000000
if n>0:
    number = x
    for i in range(n-1):
        number *= x
    print(number)     
else:
    number = x
    ans = 1
    n = abs(n)
    for i in range(n):
        if ans > 0:
            ans /= x
        else:ans = 0.0    
    print(ans)
