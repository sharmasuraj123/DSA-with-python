class Solution:
    def Reverse(self, st, s):
        if not st:
            return
        x = st.pop()
        print(x)
        s.append(x)
        self.Reverse(st, s)

    def reverseStack(self, st):
        s = []
        self.Reverse(st, s)
        return s

ob = Solution()
revS = ob.reverseStack([1,2,3,4])
print(revS)   
