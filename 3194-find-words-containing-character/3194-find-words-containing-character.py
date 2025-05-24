class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        li=[]
        for i in range(len(words)):
            if x in words[i]:
                li.append(i)
        return li