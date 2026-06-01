class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left= left
        self.right = right


def Tree():
    root = int(input("Enter root node :") )
    Queue = []
    root_node = Node(root)
    Queue.append(root_node)
    while Queue:
        left_val = int(input("enter left child_node:"))
        if left_val!=-1:
            left_node = Node(left_val)
            Queue[0].left = left_node
            Queue.append(left_node)
        right_val = int(input("enter right child_node:"))
        if right_val != -1:
            right_node = Node(right_val)
            Queue[0].right = right_node
            Queue.append(right_node)
        Queue.pop(0)
    return root_node
Tree()





