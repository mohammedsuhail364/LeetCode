class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def convert_to_num(i):
            return ord(i)-ord('a')
        s1_count=[0]*26
        s2_count=[0]*26
        for i in s1:
            idx=convert_to_num(i)
            s1_count[idx]+=1
        l=0
        for r in range(len(s2)):
            idx=convert_to_num(s2[r])
            s2_count[idx]+=1
            if (r-l+1)>len(s1):
                idx=convert_to_num(s2[l])
                s2_count[idx]-=1
                l+=1
            if (r-l+1)==len(s1) and s1_count==s2_count :
                return True
        return False