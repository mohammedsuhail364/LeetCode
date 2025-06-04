class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        n=len(word)
        length=n-numFriends+1
        result=""
        max_letter=max(word)
        for i in range(n):
            if word[i]==max_letter:
                substr=word[i:i+length]
                result=max(result,substr)
        return result
