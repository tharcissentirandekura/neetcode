class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(open,close,current):
            if open == 0 and close == 0:
                res.append(current)
                return res
            if open > 0:
                generate(open - 1, close, current + "(")
            if close > open:
                generate(open,close - 1, current + ")")

        generate(n,n,"")
        return res


