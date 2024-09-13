class Solution(object):
    def minimumKeypresses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''         
        To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.
        Each number maps to three character: 
        _ (One keypress) _ (Two keypress)  _ (Three keypress)
        Highest frequency character - map to first postion (keypress count => highest character freq)
            - How many character you can occupy to first postion in a keypad => 1 - 9
        2nd highest frequency character - map to second position  (keypress count => 2*freq)
            - How many character you can occupy to first postion in a keypad => 10-18
        .. so on
        '''
        
        counter = Counter(s)
        counter = sorted(counter.items(), key = lambda x : - x[1] )
        keyPress = 0
        
        for idx, (char, cnt) in enumerate(counter):
            if idx <= 8:
                keyPress += 1 * cnt
            elif 8 < idx <= 17:
                keyPress += 2 * cnt
            else:
                keyPress += 3 * cnt
        return keyPress
        