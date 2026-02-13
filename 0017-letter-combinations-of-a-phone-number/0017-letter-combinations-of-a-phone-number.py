class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        def dfs(i,path):
            if i>=len(digits):
                res.append(path)
                return 
            cur=letters[digits[i]]
            for ch in cur:
                dfs(i+1,path+ch) 
        dfs(0,"")
        return res