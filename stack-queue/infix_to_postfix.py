s = "(a-(b^c))+(d)"
st = []
output = ""
operators = {"^": 3, "*": 2, "/": 2, "-": 1, "+": 1}
for i in s: 
    if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57:output+=i
    elif i=='(':st.append(i)
    elif i==')':
        while st and st[-1]!='(':
            output+=st.pop()
        st.pop()
    else:
        while st and st[-1]!='(' and operators[i]<=operators[st[-1]] and i!='^':
            output += st.pop()
        st.append(i) 
while st:
    output+=st[-1]
    st.pop()
print(output)        
