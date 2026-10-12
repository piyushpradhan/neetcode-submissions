class Solution:
    def matchBracket(self, ch: str) -> str | None:
        match ch: 
            case ')':
                return '('
            case '}':
                return '{'
            case ']':
                return '['
        
    def isValid(self, s: str) -> bool:
        openBrackets = []

        for ch in s: 
            if len(openBrackets) > 0 and self.matchBracket(ch) == openBrackets[-1]:
                openBrackets.pop()
            else:
                openBrackets.append(ch)
        
        return len(openBrackets) == 0