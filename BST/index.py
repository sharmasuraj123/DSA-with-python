class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = self.right = None

root = None

def InorderTraversal(a):
    if a is None:return
    InorderTraversal(a.left)
    print(a.val,end=' ')
    InorderTraversal(a.right)

def Insert(root,val):
    if root is None: 
        return Node(val)
    if root.val>val:
        root.left = Insert(root.left,val)
    else:
        root.right = Insert(root.right,val)
    return root        

arr = [3, 2, 1, 5, 6, 4]
for i in arr:
    root = Insert(root, i)
    
InorderTraversal(root)
