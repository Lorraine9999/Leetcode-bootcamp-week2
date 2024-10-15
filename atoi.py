class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading whitespace
        s = s.lstrip()

        # If string is empty after removing whitespace, return 0
        if not s:
            return 0

        #  Determine the sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        #  Read the digits and convert to integer
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        #  Apply the sign
        result *= sign

        #  Clamp the result within the 32-bit signed integer range [-2^31, 2^31 - 1]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result