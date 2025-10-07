class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n=len(rains)
        last_rain_day={}
        res=[-1]*n
        dry_days=[]
        for i,lake in enumerate(rains):
            if lake==0:
                dry_days.append(i)
                res[i]=1
            else:
                if lake in last_rain_day:
                    found_dry_day=False
                    for dry_day in dry_days:
                        if last_rain_day[lake]<dry_day:
                            res[dry_day]=lake
                            dry_days.remove(dry_day)
                            found_dry_day=True
                            break
                    if not found_dry_day:
                        return []
                last_rain_day[lake]=i
                res[i]=-1
        return res