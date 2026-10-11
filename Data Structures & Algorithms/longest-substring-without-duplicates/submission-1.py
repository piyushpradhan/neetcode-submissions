class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        i = 0
        charDict: dict[str, int] = {}

        for ind in range(len(s)): 
            if s[ind] in charDict:
                i = max(charDict[s[ind]] + 1, i)
            charDict[s[ind]] = ind
            longestLength = max(longestLength, ind - i + 1)
        
        return longestLength