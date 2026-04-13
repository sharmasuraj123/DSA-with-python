# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0 or not lists:
#             return None
#         while len(lists) > 1:
#             pairedList = []

#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if len(lists) > i + 1 else None
#                 l = self.mergeTwoLists(l1, l2)
#                 pairedList.append(l)
#             lists = pairedList
#         return lists[0]

#     def mergeTwoLists(self, l1, l2):
#         dummy = ListNode(0)
#         tail = dummy
#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next

#         while l1:
#             tail.next = l1
#             break
#         while l2:
#             tail.next = l2
#             break
#         return dummy.next
