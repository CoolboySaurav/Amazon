from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prereq):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Create an adjacency list for the graph
        adj = defaultdict(list)
        for crs, pre in prereq:
            adj[crs].append(pre)

        # Stack to maintain the topological order
        st = []
        # Dictionary to track the state of each node: 0 = unvisited, 1 = visiting, 2 = visited
        visited = {}

        def dfs(node):
            # If node is visiting, we have a cycle
            if node in visited:
                return visited[node] == 2
            
            # Mark the node as visiting
            visited[node] = 1
            
            # Visit all the neighbors
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            # Mark the node as visited
            visited[node] = 2
            # Add the node to the stack
            st.append(node)
            return True

        # Start DFS from every unvisited node
        for num in range(numCourses):
            if num not in visited:
                if not dfs(num):
                    return []

        # Return the reverse of the stack to get the topological order
        return st
