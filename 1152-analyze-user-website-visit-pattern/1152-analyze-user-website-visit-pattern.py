from collections import defaultdict
from itertools import combinations

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # Combine username, website, and timestamp and sort by timestamp
        activity = sorted(zip(timestamp, username, website))
        
        # Build user to website visits mapping sorted by time
        userMap = defaultdict(list)
        for _, user, site in activity:
            userMap[user].append(site)
        
        # Dictionary to count patterns across all users
        patternCount = defaultdict(int)
        
        # Set to hold unique patterns to avoid duplicates per user
        for user, sites in userMap.items():
            # Generate all unique 3-sequence patterns per user
            patterns = set(combinations(sites, 3))
            for pattern in patterns:
                patternCount[pattern] += 1
        
        # Find the most visited pattern with lexicographical tie-breaking
        most_visited = min(patternCount, key=lambda x: (-patternCount[x], x))
        
        return list(most_visited)



# from collections import defaultdict

# class Solution(object):
#     def mostVisitedPattern(self, username, timestamp, website):
#         """
#         :type username: List[str]
#         :type timestamp: List[int]
#         :type website: List[str]
#         :rtype: List[str]
#         """
#         # Combine the username, website, and timestamp into a single list and sort by timestamp
#         userMap = defaultdict(list)
#         activity = [[a, b, c] for a, b, c in zip(username, website, timestamp)]
#         activity.sort(key=lambda x: x[2])  # Sort by timestamp
        
#         # Build a user-to-website mapping sorted by time
#         for user, url, _ in activity:
#             userMap[user].append(url)
        
#         # To count the occurrences of each unique 3-sequence pattern per user
#         urlMap = defaultdict(set)
        
#         # For each user, generate all possible 3-sequences
#         for user, urllist in userMap.items():
#             # To ensure unique patterns per user
#             unique_patterns = set()
#             for i in range(len(urllist) - 2):
#                 for j in range(i + 1, len(urllist) - 1):
#                     for k in range(j + 1, len(urllist)):
#                         pattern = (urllist[i], urllist[j], urllist[k])
#                         unique_patterns.add(pattern)
            
#             # Update the map with unique patterns for each user
#             for pattern in unique_patterns:
#                 urlMap[pattern].add(user)
        
#         # Determine the most visited 3-sequence pattern
#         most_visited = []
#         max_count = 0
        
#         for pattern, users in urlMap.items():
#             if len(users) > max_count or (len(users) == max_count and pattern < most_visited):
#                 most_visited = pattern
#                 max_count = len(users)
        
#         return list(most_visited)
