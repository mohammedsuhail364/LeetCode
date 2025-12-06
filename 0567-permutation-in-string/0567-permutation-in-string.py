class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def convert_index(s):
            return ord(s)-ord('a')
        if len(s1)>len(s2):
            return False
        count1=[0]*26
        count2=[0]*26
        for i in range(len(s1)):
            i1=convert_index(s1[i])
            i2=convert_index(s2[i])
            count1[i1]+=1
            count2[i2]+=1
        if count1==count2:
            return True
        # sliding window part starts
        l=0
        for r in range(len(s1),len(s2)):
            r1=convert_index(s2[r])
            count2[r1]+=1
            l1=convert_index(s2[l])
            count2[l1]-=1
            l+=1
            if count1==count2:
                return True
        return False 

