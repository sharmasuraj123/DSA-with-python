# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         hash = {}
#         i = 0
#         while head:
#             if head.next in hash:
#                 return head.next
#             hash[head] = i
#             i += 1
#             head = head.next
#         return None
