class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            "2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'
        }
        res=[]
        def dfs(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for x in letters[digits[i]]:
                dfs(i+1,cur+x)
        dfs(0,"")
        return res
