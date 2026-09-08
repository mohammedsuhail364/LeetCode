class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # refer neetcode
        nums=[1]
        i2,i3,i5=0,0,0
        for i in range(1,n):
            next_num=min(nums[i2]*2,nums[i3]*3,nums[i5]*5)
            if next_num==nums[i2]*2:
                i2+=1
            if next_num==nums[i3]*3:
                i3+=1
            if next_num==nums[i5]*5:
                i5+=1
            nums.append(next_num)
        return nums[n-1]
                