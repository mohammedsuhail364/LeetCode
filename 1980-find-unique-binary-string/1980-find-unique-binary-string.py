class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen=set(nums)
        res=''
        sen="01"
        def dfs(i,path):
            nonlocal res
            if len(path)==len(nums[0]):
                temp=''.join(path)
                if temp not in seen:
                    res=temp
                return
            if i>=len(sen):
                return
            dfs(i,path+[sen[i]])
            dfs(i+1,path)
        dfs(0,[])
        return res