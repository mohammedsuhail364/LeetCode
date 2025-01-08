class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                k=words[i]
                if words[j][:len(k)]==k and words[j][-len(k):]==k:
                    res+=1
        return res