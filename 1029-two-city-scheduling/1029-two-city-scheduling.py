class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # this question is quite interesting because in the first example it easily split into half but think of this [[10,20],[30,200],[20,400],[30,20]]
        # we have three less values in A but we want put only two so we want to choose the values for B by check their difference
        # Because sorting by difference brings:
        # most beneficial-to-send-to-A people to the front,
        # most beneficial-to-send-to-B people to the back.
        # This immediately helps divide the group into two equal halves.
        # Negative diff → send to A
        # Positive diff → send to B
        costs.sort(key=lambda x:(x[0]-x[1]))
        res=0
        half=len(costs)//2
        for index,value in enumerate(costs):
            a,b = value
            if index<half:
                res+=a
            else:
                res+=b
        return res
