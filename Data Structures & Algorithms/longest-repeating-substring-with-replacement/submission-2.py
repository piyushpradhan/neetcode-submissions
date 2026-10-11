class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        stringSet = set(s)

        for ch in stringSet:
            count = left = 0 
            for right in range(len(s)):
                if s[right] == ch:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == ch:
                        count -= 1
                    left += 1

                result = max(result, right - left + 1)
        
        return result
