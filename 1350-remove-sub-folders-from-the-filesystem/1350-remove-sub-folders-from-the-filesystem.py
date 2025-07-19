class Solution:
    def removeSubfolders(self, folder) :
        res=[]
        folder.sort()
        for path in folder:
            if not res or not path.startswith(res[-1]+"/"):
                res.append(path)

        return res