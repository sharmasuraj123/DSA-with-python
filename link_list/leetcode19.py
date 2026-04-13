# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if head is None:
#             return head
#         elif head.next is None:
#             return None
#         length = 0
#         node = head
#         while node:
#             length += 1
#             node = node.next
#         idx = 0
#         target = length - n
#         if target == 0:
#             head = head.next
#             return head
#         node = head
#         while idx != target - 1:
#             node = node.next
#             idx += 1
#         node.next = node.next.next
#         return head
