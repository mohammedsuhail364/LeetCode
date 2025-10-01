class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.operations={
            "+":lambda x,y:x+y,
            "-":lambda x,y:x-y,
            "*":lambda x,y:x*y
        }
        def dfs(exp):
            res=[]
            for i,ch in enumerate(exp):
                if ch in "-+*":
                    left_results=dfs(exp[:i])
                    right_results=dfs(exp[i+1:])
                    for l in left_results:
                        for r in right_results:
                            res.append(self.operations[ch](l,r))
            if not res:
                res.append(int(exp))
            return res                
        return dfs(expression)