from collections import defaultdict

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # Combine the username, website, and timestamp into a single list and sort by timestamp
        userMap = defaultdict(list)
        activity = [[a, b, c] for a, b, c in zip(username, website, timestamp)]
        activity.sort(key=lambda x: x[2])  # Sort by timestamp
        
        # Build a user-to-website mapping sorted by time
        for user, url, _ in activity:
            userMap[user].append(url)
        
        # To count the occurrences of each unique 3-sequence pattern per user
        urlMap = defaultdict(set)
        
        # For each user, generate all possible 3-sequences
        for user, urllist in userMap.items():
            # To ensure unique patterns per user
            unique_patterns = set()
            for i in range(len(urllist) - 2):
                for j in range(i + 1, len(urllist) - 1):
                    for k in range(j + 1, len(urllist)):
                        pattern = (urllist[i], urllist[j], urllist[k])
                        unique_patterns.add(pattern)
            
            # Update the map with unique patterns for each user
            for pattern in unique_patterns:
                urlMap[pattern].add(user)
        
        # Determine the most visited 3-sequence pattern
        most_visited = []
        max_count = 0
        
        for pattern, users in urlMap.items():
            if len(users) > max_count or (len(users) == max_count and pattern < most_visited):
                most_visited = pattern
                max_count = len(users)
        
        return list(most_visited)
