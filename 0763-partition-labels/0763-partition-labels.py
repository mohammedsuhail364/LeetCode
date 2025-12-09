class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # in this question we observe one thing like if we take a first character 'a' it ends in index 8 that time we can include character from 0 - 8 to make a partition but one thing if the second or third letter has a last index is 10 or 12 that time we can include that also the same partition it is the main intuation 
        last={s[i]:i for i in range(len(s))} # find the last occurrence of the characters
        start=0
        res=[]
        max_index=0
        for i in range(len(s)):
            max_index=max(max_index,last[s[i]])
            if i == max_index:
                res.append(i-start+1) # length of the word
                start=i+1
        return res