class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res=[pref[0]]
        for i in range(1,len(pref)):
            res.append(pref[i-1]^pref[i])
        return res