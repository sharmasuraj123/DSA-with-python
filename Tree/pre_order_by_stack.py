
st,res = [],[]
st.append(root)
res.append(root.val)
while len(st)>1:
    if st[-1].left!=None:
        res.append(st[-1].left.val)
        st.append(st[-1].left)
    elif st[-1].right!=None:
        res.append(st[-1].right.val)
        st.append(st[-1].right)
    else:
        st.pop()
        st[-1].left = None
print(res)        
        