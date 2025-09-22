class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        the main observation is we dont go for backtrack it is impossible to implement and the intuation is we can split into two or more with the length of three with including all the elements in the array so we can check every element in the nums if we can make a sequence or previous subsequence is wait for this eg: [1,2,3,3,4,4,5]
        in this we can make a subsequence at start like [1,2,3] then 4 th element comes we can make another subsequence but the 3 is waiting for 4(3+1) so if the 4 comes it goes to first subsequence then another 4 goes to another subsequence
        once debug it then understand easily
        """
        if len(nums)<3:
            return False
        freq=Counter(nums)
        subsequece=defaultdict(int)
        for i in nums:
            if freq[i]==0:
                continue
            freq[i]-=1
            if subsequece[i-1]>0:
                subsequece[i-1]-=1
                subsequece[i]+=1
            elif freq[i+1] and freq[i+2]:
                freq[i+1]-=1
                freq[i+2]-=1
                subsequece[i+2]+=1
            else:
                return False
        return True