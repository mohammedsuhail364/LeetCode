class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        # rank is not needed
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            parent[py]=px
        email_to_name={}
        for account in accounts:
            name=account[0]
            emails=account[1:]
            for email in emails:
                if email not in parent:
                    parent[email]=email
                email_to_name[email]=name
            for i in range(1,len(emails)):
                union(emails[0],emails[i]) # attach with the first email
        result=[]
        root_to_emails=defaultdict(list)
        for email in parent:
            root=find(email)
            root_to_emails[root].append(email)
        for root,emails in root_to_emails.items():
            name=email_to_name[root]
            result.append([name]+sorted(emails))
        return result
            
        

