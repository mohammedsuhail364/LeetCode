from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=inf
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # land->water
                land_end=landStartTime[i]+landDuration[i]
                water_start=max(land_end,waterStartTime[j])
                res=min(res,water_start+waterDuration[j])
                # water->land
                water_end=waterStartTime[j]+waterDuration[j]
                land_start=max(water_end,landStartTime[i])
                res=min(res,land_start+landDuration[i])
        return res
