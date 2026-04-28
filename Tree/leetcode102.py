def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    res = []
    q = []
    root_node = [root.val]
    res.append(root_node)
    q.append(root)
    while q:
        level, n = [], len(q)
        for i in range(n):
            if q[0].left != None:
                level.append(q[0].left.val)
                q.append(q[0].left)
            if q[0].right != None:
                level.append(q[0].right.val)
                q.append(q[0].right)
            q.pop(0)
        if level:
            res.append(level.copy())
    return res
