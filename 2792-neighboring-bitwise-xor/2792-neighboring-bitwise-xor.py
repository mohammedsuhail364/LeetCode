class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # refer neetcode
        first=0
        last=0
        for n in derived:
            if n==1:
                last=~last
        return first==last