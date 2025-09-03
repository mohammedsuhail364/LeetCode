class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def process(word):
            if not word:
                return [], []
            chars,counts=[word[0]],[1]
            for i in range(1,len(word)):
                if word[i]==chars[-1]:
                    counts[-1]+=1
                else:
                    chars.append(word[i])
                    counts.append(1)
            return chars,counts
        s_chars,s_counts=process(s)
        res=0
        for word in words:
            w_chars,w_counts=process(word)
            if s_chars==w_chars:
                counter=0
                for k in range(len(w_chars)):
                    if (w_counts[k]==s_counts[k] or (w_counts[k]<s_counts[k] and s_counts[k] >=3 )):
                        counter+=1
                if counter==len(w_chars):
                    res+=1
        return res