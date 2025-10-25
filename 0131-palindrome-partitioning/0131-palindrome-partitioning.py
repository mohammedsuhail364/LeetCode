class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def dfs(i):
            if i>=len(s):
                res.append(part[:])
                return
            for j in range(i,len(s)):
                if self.is_palidrome(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    def is_palidrome(self,s,l,r)->bool:
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True