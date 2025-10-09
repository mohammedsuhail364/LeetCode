class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # refer https://www.youtube.com/watch?v=2MRqK2cRmYA
        n=len(skill)
        time=[0]*n
        for m in mana:
            time[0]=time[0]+(skill[0]*m)
            for i in range(1,len(time)):
                time[i]=max(time[i],time[i-1])+skill[i]*m
            for i in range(n-2,-1,-1):
                time[i]=time[i+1]-skill[i+1]*m
        return time[-1]