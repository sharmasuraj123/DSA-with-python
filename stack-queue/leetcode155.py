# from queue import LifoQueue


# class MinStack:

#     def __init__(self):
#         self.st = LifoQueue()
#         self.full_st = LifoQueue()

#     def push(self, val: int) -> None:
#         if self.st.empty():
#             self.st.put(val)
#         else:
#             x = self.st.get()
#             self.st.put(x)
#             if x >= val:
#                 self.st.put(val)
#         self.full_st.put(val)

#     def pop(self) -> None:
#         x = self.st.get()
#         y = self.full_st.get()
#         if x != y:
#             self.st.put(x)

#     def top(self) -> int:
#         if not self.full_st.empty():
#             x = self.full_st.get()
#             self.full_st.put(x)
#             return x

#     def getMin(self) -> int:
#         if not self.st.empty():
#             x = self.st.get()
#             self.st.put(x)
#             return x


# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(val)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()
