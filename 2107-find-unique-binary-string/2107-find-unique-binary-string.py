class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        n = len(nums[0])
        res=[]
        values='01'
        def backtrack(i,n):
            if len(i)==n:
                k=''.join(i)
                if k not in nums:
                    res.append(k)
                    return True
                return False
            for x in values:
                i.append(x)
                if backtrack(i,n):
                    return True
                i.pop()
        backtrack([],n)
        return res[0]