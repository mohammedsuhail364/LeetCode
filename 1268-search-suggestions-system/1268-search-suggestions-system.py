class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # without Trie we have go with a solution like a binary search thing
        words = sorted(products)
        l = 0
        r = len(words)-1
        res=[]
        for i in range(len(searchWord)):
            c = searchWord[i]
            # move the left pointer
            while l<=r and (len(words[l])<=i or c != words[l][i]):
                l+=1
            while l<=r and (len(words[r])<=i or c != words[r][i]):
                r-=1
            all_words = words[l:r+1]
            res.append( all_words[:3])
        return res