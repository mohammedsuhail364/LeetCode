class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        def backtrack(path):
            nonlocal k
            if len(path)==n :
                k-=1
                if k==0:
                    return ''.join(path)
                return
            for j in 'abc':
                if path and path[-1]==j:
                    continue
                res = backtrack(path+[j])
                if res:
                    return res
            return ''
        return backtrack([])