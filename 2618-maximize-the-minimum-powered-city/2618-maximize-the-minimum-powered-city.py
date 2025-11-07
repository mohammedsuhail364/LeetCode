class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # refer neetcode
        n=len(stations)
        # make a diff array
        diff=[0]*(n+1)
        for i in range(n):
            left=max(0,i-r)
            right=min(n,i+r+1) # line sweep
            diff[left]+=stations[i]
            diff[right]-=stations[i]
        
        def can_acheive(target_p):
            cur_p=0
            cur_k=k
            diff_copy=diff[:]
            for i in range(n):
                cur_p+=diff_copy[i]
                if cur_p<target_p:
                    additional = target_p-cur_p
                    if additional > cur_k:
                        return False
                    cur_k-=(additional)
                    cur_p+=additional
                    right=min(n,i+2*r+1)
                    diff_copy[right]-=additional
            return True
        low,high=min(stations),sum(stations)+k
        res=low
        while low<=high:
            target_p=(low+high)//2
            if can_acheive(target_p):
                res=target_p
                low=target_p+1
            else:
                high=target_p-1
        return res