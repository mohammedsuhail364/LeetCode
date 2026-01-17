class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index={c:i for i, c in enumerate(s)}
        stack=[]
        seen=set()
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1]>s[i] and i<last_index[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return ''.join(stack)
