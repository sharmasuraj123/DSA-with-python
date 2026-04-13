s = "a*(b+c)/d"
operator = {"^":3,"/":2,"*":2,"+":1,"-":1}
s = "".join(reversed(s))
str = ''
for i in s:
    if i == ')':
        str+="("
    elif i == "(":
        str+=")"
    else:str+=i       

st,output = [],""
for i in str:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':output+=i
    elif i=="(":st.append(i)
    elif i==")":
        while st and st[-1]!="(":
            output+=st.pop()
        st.pop()    
    else:
        while (st and st[-1]!="(") and (operator[st[-1]]>operator[i] or (operator[st[-1]]==operator[i] and i=="^") ):
            output+=st.pop()
        st.append(i)
while st:
    output+=st.pop()
output = "".join(reversed(output))
print(output)
