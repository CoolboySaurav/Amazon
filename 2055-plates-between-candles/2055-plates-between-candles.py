class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Preprocess the string to find nearest candles to the left and right
        n = len(s)
        left_nearest = [-1] * n  # nearest candle to the left of every position
        right_nearest = [-1] * n  # nearest candle to the right of every position
        prefix_plates = [0] * n   # prefix sum of plates between candles

        # Fill left_nearest and prefix_plates
        left = -1  # keeps track of the last seen candle from the left
        for i in range(n):
            if s[i] == '|':
                left = i
            left_nearest[i] = left
            prefix_plates[i] = prefix_plates[i - 1] + (1 if s[i] == '*' else 0)

        # Fill right_nearest
        right = -1  # keeps track of the last seen candle from the right
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                right = i
            right_nearest[i] = right

        # Step 2: Answer each query using precomputed values
        res = []
        for left, right in queries:
            l_candle = right_nearest[left]  # first candle on or after left
            r_candle = left_nearest[right]  # last candle on or before right

            if l_candle == -1 or r_candle == -1 or l_candle >= r_candle:
                # No valid candles in the range, or candles are not properly placed
                res.append(0)
            else:
                # Number of plates between the candles
                res.append(prefix_plates[r_candle] - prefix_plates[l_candle])

        return res
