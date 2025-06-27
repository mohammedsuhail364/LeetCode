class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_valid(word):
            i=0
            count=0
            for ch in s:
                if i<len(word) and ch==word[i]:
                    i+=1
                    if i==len(word):
                        count+=1
                        i=0
                        if count==k:
                            return True
            return False

        q=deque([""])
        res=""
        while q:
            curr=q.popleft()
            for ch in range(26):
                ch=chr(ch+ord('a'))
                nxt=curr+ch
                if is_valid(nxt):
                    res=nxt
                    q.append(nxt)
        return res