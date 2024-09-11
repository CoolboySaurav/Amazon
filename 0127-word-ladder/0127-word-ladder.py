class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
    
        q = deque([(beginWord, 1)])
        
        while q:
            word, step = q.popleft()
            
            if word == endWord:
                return step
            
            for i in range(len(word)):
                left = word[: i]
                right = word[i + 1:]
                for j in range(ord('a'), ord('z') + 1):
                    temp = left + chr(j) + right
                    if temp in wordList:
                        wordList.remove(temp)
                        q.append([temp, step + 1])
        return 0