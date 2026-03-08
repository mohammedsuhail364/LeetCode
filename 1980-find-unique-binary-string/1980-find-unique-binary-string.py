class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen=set(nums)
        sen="01"
        def dfs(path):
            if len(path)==len(nums[0]):
                temp=''.join(path)
                if temp not in seen:
                    return temp
                return None
            for bit in ["0","1"]:
                res=dfs(path+[bit])
                if res:
                    return res
        return dfs([])