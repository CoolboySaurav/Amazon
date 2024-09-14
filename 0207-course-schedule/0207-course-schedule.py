

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit = {}
        
        def dfs(node):
            if node in visit:
                return visit[node] == 2
            
            visit[node] = 2
            
            for pre in adj[node]:
                if dfs(pre):
                    return True
            
            visit[node] = 1
            return False
        
        for n in range(numCourses):
            if dfs(n):
                return False
        return True