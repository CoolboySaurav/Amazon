class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        wordMap = defaultdict(list)  # Dictionary to store grouped anagrams
        
        for word in strs:
            charMap = [0] * 26  # Initialize a count array for each letter in the alphabet
            for c in word:
                ind = ord(c) - ord('a')  # Calculate the index for the character
                charMap[ind] += 1  # Increment the count for the character
            wordMap[tuple(charMap)].append(word)  # Use the character count tuple as the key
        
        return list(wordMap.values())  # Convert dictionary values to a list and return
