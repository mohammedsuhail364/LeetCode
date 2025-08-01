class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l=len(words[0])
        total=l*len(words)
        def freq_map(word_list):
            tmp={}
            for i in word_list:
                if i not in tmp:
                    tmp[i]=0
                tmp[i]+=1
            return tmp
        res=[]
        main_map=freq_map(words)
        for start in range(len(s)-total+1):
            cur_list=[]
            for i in range(start,start+total,l):
                cur_list.append(s[i:i+l])
            if freq_map(cur_list)==main_map:
                res.append(start)
        return res