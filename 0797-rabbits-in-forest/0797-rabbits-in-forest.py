class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for i, j in count.items():
            group_size=(i+1)
            groups=ceil(j/group_size)
            res+=(groups*group_size)
        return res