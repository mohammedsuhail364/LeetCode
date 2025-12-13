from typing import List
from heapq import heappush
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def validate(code):
            if not code:
                return False
            for c in code:
                if c=="_":
                    continue
                if not c.isalnum():
                    return False
            return True
        category={i:[] for i in ["electronics", "grocery", "pharmacy", "restaurant"]}
        for i in range(len(code)):
            if not validate(code[i]):
                continue
            if not isActive[i]:
                continue
            if businessLine[i] not in category:
                continue
            category[businessLine[i]].append(code[i])
        res=[]
        for v in category.values():
            res+=(sorted(v))
        return res