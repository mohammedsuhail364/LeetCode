class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # refer this https://www.youtube.com/watch?v=oJVnC_kvFcI
        n=len(s)
        left=[[0]*3 for _ in range(n)] # [partition,mask,distinct]
        right=[[0]*3 for _ in range(n)] # [partition,mask,distinct]
        # compute prefix
        partition=0
        mask=0
        distinct=0
        for i in range(n-1):
            bit=1<<(ord(s[i])-ord('a'))
            if mask&bit==0:
                distinct+=1
                if distinct<=k:
                    mask=mask|bit
                else:
                    partition+=1
                    mask=bit
                    distinct=1
            left[i+1][0]=partition
            left[i+1][1]=mask
            left[i+1][2]=distinct
        # compute prefix
        partition=0
        mask=0
        distinct=0
        for i in range(n-1,0,-1):
            bit=1<<(ord(s[i])-ord('a'))
            if mask&bit==0:
                distinct+=1
                if distinct<=k:
                    mask=mask|bit
                else:
                    partition+=1
                    mask=bit
                    distinct=1
            right[i-1][0]=partition
            right[i-1][1]=mask
            right[i-1][2]=distinct
        # combine and calculate
        max_partition=0
        for i in range(n):
            total=left[i][0]+right[i][0]+2
            combine_mask=left[i][1]|right[i][1]
            combine_bit_count=bin(combine_mask).count('1')
            if left[i][2]==k and right[i][2]==k and combine_bit_count<26:   
                total+=1
            elif min(combine_bit_count+1,26)<=k:
                total-=1
            max_partition=max(max_partition,total)
        return max_partition