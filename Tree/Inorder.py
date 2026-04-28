# class Node:
#     def __init__(self, val, left=0, right=0):
#         self.val = val
#         self.left = left
#         self.right = right


# def Tree():
#     val = int(input("enter the node: "))
#     if val == -1:
#         return None
#     new_node = Node(val)
#     new_node.left = Tree()
#     new_node.right = Tree()
#     return new_node


# def Inorder(root_node):
#     if root_node == None:
#         return
#     Inorder(root_node.left)
#     print(root_node.val)
#     Inorder(root_node.right)


# root = Tree()
# Inorder(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

#         # moris traversal

#         if root is None:
#             return []
#         res, curr = [], root
#         while curr:
#             if curr.left == None:
#                 res.append(curr.val)
#                 curr = curr.right

#             else:
#                 # find Ip
#                 ip = curr.left
#                 while ip.right != None and ip.right != curr:
#                     ip = ip.right

#                 if ip.right == None:
#                     ip.right = curr
#                     curr = curr.left
#                 else:
#                     ip.right = None
#                     res.append(curr.val)
#                     curr = curr.right
#         return res

        # #using stack
        # if root is None:return []

        # res,st = [],[]
        # st.append(root)
        # res = []
        # while st:
        #     if st[-1] is not None:
        #         st.append(st[-1].left)
        #         continue
        #     if st :st.pop()
        #     if st:
        #         node = st.pop()
        #         res.append(node.val)
        #         st.append(node.right)

        # return res

        # r = []
        # def traverse(root):
        #     if root is None:return
        #     traverse(root.left)
        #     r.append(root.val)
        #     traverse(root.right)
        # traverse(root)
        # return r
