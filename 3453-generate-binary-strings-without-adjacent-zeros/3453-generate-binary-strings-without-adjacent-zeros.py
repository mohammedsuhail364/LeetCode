class Solution:
    def validStrings(self, n: int) :
        self.res=[]
        def backtrack(li):
            if len(li)==n:
                self.res.append(''.join(li))
                return
            if not li or li[-1]!='0' :
                li.append('0')
                backtrack(li)
                li.pop()
            
            if len(li)<n:
                li.append("1")
                backtrack(li)
                li.pop()
        backtrack([])
        return self.res