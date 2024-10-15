class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        p_count = Counter(p)
        s_count = Counter(s[:len(p)-1])
        result = []
        
        for i in range(len(p) - 1, len(s)):
            # Add the new character to the current window
            s_count[s[i]] += 1
            
            # If the two counts are equal, it's an anagram
            if s_count == p_count:
                result.append(i - len(p) + 1)
            
            # Remove the character that's sliding out of the window
            s_count[s[i - len(p) + 1]] -= 1
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]
        
        return result
