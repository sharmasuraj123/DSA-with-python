class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # using stack(reverse of the preorder by st)
        if root is None:
            return []
        res, st = [], []
        st.append(root)
        res = []
        while st:
            node = st.pop()
            res.append(node.val)
            if node.left != None:
                st.append(node.left)
            if node.right != None:
                st.append(node.right)
        res.reverse()

        return res

        # r = []
        # def traverse(root):
        #     if root is None:return
        #     traverse(root.left)
        #     traverse(root.right)
        #     r.append(root.val)
        # traverse(root)
        # return r
