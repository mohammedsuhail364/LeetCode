class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sortTheArray(num):
            res=0
            while num:
                tmp = num%10
                res += tmp
                num=num//10
            return res 
        target = sorted(nums,key = lambda x:(sortTheArray(x),x))
        pos={v:i for i,v in enumerate(target)}
        
        perm = [ pos[v] for v in nums]
        n = len(nums)
        visited = [False]*n
        swaps = 0
        for i in range(n):
            if visited[i]:
                continue
            j=i
            cycle_len = 0
            while not visited[j]:
                visited[j]=True
                cycle_len+=1
                j=perm[j]
            swaps+=cycle_len-1
        return swaps
