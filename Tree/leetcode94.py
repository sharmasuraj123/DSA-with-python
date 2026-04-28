def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    # using stack
    res, st = [], []
    st.append(root)
    res = []
    while st:
        if st[-1] is not None:
            st.append(st[-1].left)
            continue
        if st:
            st.pop()
        if st:
            node = st.pop()
            res.append(node.val)
            st.append(node.right)

    return res

    # r = []
    # def traverse(root):
    #     if root is None:return
    #     traverse(root.left)
    #     r.append(root.val)
    #     traverse(root.right)
    # traverse(root)
    # return r
