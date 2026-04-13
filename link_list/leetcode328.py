#  if head == None or head.next==None:return head
#         List = []
#         pivot = head
#         while pivot and pivot.next:
#             List.append(pivot.val)
#             pivot = pivot.next.next
#         if pivot !=None:List.append(pivot.val)    
#         pivot = head.next
#         while pivot and pivot.next:
#             List.append(pivot.val)
#             pivot = pivot.next.next
#         if pivot !=None:List.append(pivot.val)
#         pivot = head
#         i = 0
#         while pivot:
#             pivot.val = List[i]  
#             i+=1
#             pivot = pivot.next
#         return head     