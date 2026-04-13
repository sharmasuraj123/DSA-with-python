class Solution:

    def GenerateAllPar(self, curr, open, close, res, n):
        if len(curr) == 2 * n:
            res.append(curr)
            return

        if open < n:
            self.GenerateAllPar(curr + "(", open + 1, close, res, n)
        if close < open:
            self.GenerateAllPar(curr + ")", open, close + 1, res, n)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.GenerateAllPar("", 0, 0, res, n)
        return res

    # def isValid(self,s):
    #     count = 0
    #     for i in s:
    #         if i=="(":count+=1
    #         else:count-=1
    #         if count<0:return False
    #     return False if count!=0 else True

    # def GenerateAllPar(self,curr,res,n):
    #     if len(curr)==2*n:
    #         if self.isValid(curr):
    #             res.append(curr)
    #         return
    #     self.GenerateAllPar(curr+'(',res,n)
    #     self.GenerateAllPar(curr+')',res,n)

    # def generateParenthesis(self, n: int) -> List[str]:
    #     res = []
    #     self.GenerateAllPar("",res,n)
    #     return res
