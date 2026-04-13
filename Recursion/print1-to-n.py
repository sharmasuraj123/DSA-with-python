def Print(n):
    if n==0:
        return
    print(n)
    Print(n-1)
    print(n)

Print(6)    
