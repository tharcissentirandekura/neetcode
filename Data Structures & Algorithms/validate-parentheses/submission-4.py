class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        if len(s) == 1:
            return False
        for par in s:
            if par in parenthesis.values():
                if stack:
                    prev = stack.pop()
                    if par != parenthesis[prev]:
                        return False
                else:
                    return False
            if par in parenthesis:
                stack.append(par)
        return len(stack) == 0



        