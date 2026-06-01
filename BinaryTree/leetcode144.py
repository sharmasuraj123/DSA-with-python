def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # Iterative Preorder traversal(using stack)
    if root == None:
        return []
    st, res = [root], []
    while st:
        node = st.pop()
        res.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return res

    # r = []
    # def traverse(root):
    #     if root is None:return
    #     r.append(root.val)
    #     traverse(root.left)
    #     traverse(root.right)
    # traverse(root)
    # return r
