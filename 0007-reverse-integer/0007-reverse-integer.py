class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        num = 0
        
        while temp:
            num = (num* 10) + temp % 10
            temp = temp // 10
        
        if x < 0: num = - num
        return num if INT_MIN <= num <= INT_MAX else 0