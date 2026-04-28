class Node:
    def __init__(self,val,left=0,right=0):
        self.val = val
        self.left = left 
        self.right = right 

def Tree():
    val = int(input("enter the node: "))
    if val == -1:
        return None
    new_node = Node(val)
    new_node.left = Tree()
    new_node.right = Tree()
    return new_node

def preorder(root_node):
    if root_node==None:return 
    print(root_node.val)
    preorder(root_node.left)
    preorder(root_node.right)


root = Tree()
preorder(root)
