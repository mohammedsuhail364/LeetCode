from typing import List

from collections import defaultdict
from heapq import heappop,heappush
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap=[]
        self.task_to_priority={}
        self.task_to_userId={}
        for u,t,p in tasks:
            self.task_to_priority[t]=p
            self.task_to_userId[t]=u
            heappush(self.heap,(-p,-t,u))
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_priority[taskId]=priority
        self.task_to_userId[taskId]=userId
        heappush(self.heap,(-priority,-taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId]=newPriority
        userId=self.task_to_userId[taskId]
        heappush(self.heap,(-newPriority,-taskId,userId))
    def rmv(self, taskId: int) -> None:
        del self.task_to_priority[taskId]
        del self.task_to_userId[taskId]
        

    def execTop(self) -> int:
        while self.heap:
            p,t,u=heappop(self.heap)
            priority=-p
            taskId=-t
            if taskId in self.task_to_priority and self.task_to_priority[taskId]==priority and self.task_to_userId[taskId] == u :
                del self.task_to_priority[taskId]
                del self.task_to_userId[taskId] 
                return u
        return -1