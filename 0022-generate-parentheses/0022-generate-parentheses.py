class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # this question is basically try all possibilities
        # 1.always try open parenthesis
        # 2.if open has exists then we try the closed parenthesis
        # 3.if open and close has same count of n then append the res and return
        res=[]
        def dfs(arr,opened,close):
            if opened==close==n:
                res.append(arr)
                return
            if opened<n:
                dfs(arr+"(",opened+1,close)
            if opened>close:
                dfs(arr+')',opened,close+1)
        dfs("",0,0)
        return res