class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # “When is it safe to REMOVE a character I already took?”
        stack=[]
        seen=set()
        last_index={c:i for i,c in enumerate(s)} # this map ensure the last index of every character
        for i,c in enumerate(s):
            if c in seen:
                continue # this line ensures the existing character is te correct one
            while stack and stack[-1] > c and i<last_index[stack[-1]]:
                # when we can pop the element
                # Current character < stack top (improves lexicographic order)
                # The stack top appears later again in the string
                # Removing it won’t lose uniqueness
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)