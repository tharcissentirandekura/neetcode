class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # valid arithmetix expression in reverse polish Notation
        def parseTokenOperator(token, a,b):
            if token == '+':
                return a + b
            elif token == '-':
                return a - b
            elif token == '*':
                return a * b
            elif token == '/':
                return a / b
        stack = []
        operators = ["+", "-", "*","/"]
        for token in tokens:
            if token in operators:
                # pop 2 numbres
                first = stack.pop()
                second = stack.pop()
                res = parseTokenOperator(token, int(second), int(first))
                print(second,first,token)
                stack.append(res) 
            else:
                stack.append(token)
        print(stack[-1])
        return int(stack[-1])