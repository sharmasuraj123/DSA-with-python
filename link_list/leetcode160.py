# class Solution:
#     def getIntersectionNode(
#         self, headA: ListNode, headB: ListNode
#     ) -> Optional[ListNode]:
#         n1, n2 = 0, 0
#         pivot1, pivot2 = headA, headB
#         while pivot1:
#             n1 += 1
#             pivot1 = pivot1.next
#         while pivot2:
#             n2 += 1
#             pivot2 = pivot2.next
#         if n1 > n2:
#             i = n1 - n2
#             while i:
#                 headA = headA.next
#                 i -= 1
#         else:
#             i = n2 - n1
#             while i:
#                 headB = headB.next
#                 i -= 1
#         while headA:
#             if headA == headB:
#                 return headA
#             headA = headA.next
#             headB = headB.next
#         return None
