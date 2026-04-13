# class Solution:
#     def segregate(self, head):
#         count0, count1, count2 = 0, 0, 0
#         pivot = head
#         while pivot:
#             if pivot.data == 0:
#                 count0 += 1
#                 pivot = pivot.next
#             elif pivot.data == 1:
#                 count1 += 1
#                 pivot = pivot.next
#             else:
#                 count2 += 1
#                 pivot = pivot.next
#         pivot = head
#         while count0:
#             pivot.data = 0
#             pivot = pivot.next
#             count0 -= 1
#         while count1:
#             pivot.data = 1
#             pivot = pivot.next
#             count1 -= 1
#         while count2:
#             pivot.data = 2
#             pivot = pivot.next
#             count2 -= 1
#         return head
