class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        di=defaultdict(int)
        for email in emails:
            e_o=email.split('@')[1]
            e=email.split('@')[0]
            temp=""
            for i in e:
                if i=='.':
                    continue
                elif i=="+":
                    break
                else:
                    temp+=i
            tmp=temp+'@'+e_o
            di[tmp]+=1
        return len(di)
            