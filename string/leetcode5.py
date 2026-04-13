s ="babad"
max_str = ""
max_length = 0
n = len(s)
for i in range(n):
    # for odd length
    a,b = i,i
    while a>=0 and b<n and s[a]==s[b]:
        if (b-a+1)>max_length:
            max_length = b-a+1
            max_str = s[a:b+1]
        a-=1
        b+=1

    # for even length
    a,b = i,i+1
    while a >= 0 and b < n and s[a] == s[b]:
        if (b - a + 1) > max_length:
            max_length = b - a + 1
            max_str = s[a : b + 1]
        a -= 1
        b += 1

print(max_length)        
 