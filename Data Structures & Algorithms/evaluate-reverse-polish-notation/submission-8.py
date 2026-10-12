class Solution:
    def evaluate(self, operator: str, operandi: List[str]) -> int | None:
        b = int(operandi.pop())
        a = int(operandi.pop())

        match operator:
            case '*':
                return a * b
            case '-':
                return a - b
            case '/':
                quotient = abs(a) // abs(b)
                return -quotient if (a < 0) != (b < 0) else quotient
            case '+':
                return a + b

    def evalRPN(self, tokens: List[str]) -> int:
        pending = []
        operators = {'+', '-', '/', '*'}

        for token in tokens:
            if token in operators:
                result = self.evaluate(token, pending)
                pending.append(result)
            else:
                pending.append(token)

        return int(pending[0])
