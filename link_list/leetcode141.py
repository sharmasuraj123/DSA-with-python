# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         Set = set()
#         while head:
#             if head.next in Set:
#                 return True
#             Set.add(head)
#             head = head.next
#         return False


hash = {}
head = 4
hash[head] = 5
print(hash)
if 5 in hash:
    print("true")
