class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        res=[]
        def dfs(i,path):
            if i==len(s):
                path=' '.join(path)
                res.append(path)
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word in wordDict:
                    path.append(word)
                    dfs(j+1,path)
                    path.pop()
        dfs(0,[])
        return res