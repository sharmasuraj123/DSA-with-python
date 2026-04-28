class Node:
    def __init__(self, val, left=0, right=0):
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


def Postorder(root_node):
    if root_node == None:
        return
    Postorder(root_node.left)
    Postorder(root_node.right)
    print(root_node.val)

root = Tree()
Postorder(root)
