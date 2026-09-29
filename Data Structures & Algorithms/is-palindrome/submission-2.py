class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted: str = ""
        for ch in s: 
            if ch.isalnum():
                formatted = formatted + ch.lower()
        
        return formatted[::-1] == formatted