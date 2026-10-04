class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs(i,opened,closed):
            if i>=len(s):
                return opened==closed
            if opened<closed:
                return False
            a,b,c=False,False,False
            if s[i]=="(":
                a=dfs(i+1,opened+1,closed)
            elif s[i]==")":
                if closed<opened:
                    b= dfs(i+1,opened,closed+1)
                else:
                    return False
            elif s[i]=="*":
                c = (dfs(i+1,opened+1,closed) or 
                dfs(i+1,opened,closed+1)or
                dfs(i+1,opened,closed))
            return a or b or c 
        return dfs(0,0,0)