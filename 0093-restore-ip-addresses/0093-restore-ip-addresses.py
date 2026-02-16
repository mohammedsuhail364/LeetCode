class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def dfs(i,path):
            if i==len(s):
                if len(path)==4:
                    path=''.join(path)
                    res.append(path[:-1])
                return
            for j in range(i,len(s)):
                if self.isValid(s,i,j):
                    path.append(s[i:j+1]+'.')
                    dfs(j+1,path)
                    path.pop()
        dfs(0,[])
        return res
    def isValid(self,s,i,j):
        val=s[i:j+1]
        if int(val)>255 or val in '@' or (len(val)>1 and val[0]=='0'):
            return False
        return True
        