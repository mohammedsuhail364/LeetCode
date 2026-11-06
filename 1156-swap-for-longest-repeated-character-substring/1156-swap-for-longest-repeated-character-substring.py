class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # this question is sliding window with 1 character replacement but check for all distinct characters which involve in this text
        res=0
        freq=Counter(text)
        for ch in freq:
            l=0
            c=0
            for r in range(len(text)):
                if text[r]==ch:c+=1
                while (r-l+1) - c > 1: # which have one different character others are same 
                    if text[l]==ch:
                        c-=1
                    l+=1
                res=max(res,min(r-l+1,freq[ch])) # why the inner check is , is we replace this char or not because the window size is 4 with one different char but the total freq of ch is 3 at the time we dont chars to replace
        return res