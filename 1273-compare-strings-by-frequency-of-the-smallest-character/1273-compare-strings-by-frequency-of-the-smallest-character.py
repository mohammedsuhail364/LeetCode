class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(word):
            x=sorted(Counter(word).items())
            return x[0][1]
        res=[0]*len(queries)
        count_query=[]
        count_word=[]
        for i in range(len(queries)):
            query=queries[i]
            count_query.append(helper(query))
        for i in range(len(words)):
            word=words[i]
            count_word.append(helper(word))
        count_word.sort(reverse=True)
        i=0
        while i<len(count_query):
            j=0
            while j<len(count_word) and count_query[i]<count_word[j]:
                j+=1
            res[i]=j
            i+=1
        return res