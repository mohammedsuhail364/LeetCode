class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        res=[-1]*n
        full={}
        dry_days=[]
        for i,lake in enumerate(rains):
            if lake==0:
                bisect.insort(dry_days,i)
                res[i]=1
            else:
                if lake in full:
                    idx=bisect.bisect_right(dry_days,full[lake]) # to find the dry is inbetween the last fill and current
                    if idx==len(dry_days): # means no dry day for this 
                        return []
                    dry_day=dry_days[idx]
                    res[dry_day]=lake
                    dry_days.pop(idx)
                full[lake]=i
                res[i]=-1
        return res