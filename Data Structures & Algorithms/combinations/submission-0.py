class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def generate(i,curr):
            if len(curr) == k:
                # done generate this
                res.append(curr.copy())
                return 
            
            # if i > n:
            #     return 
            
            for j in range(i,n + 1):
                curr.append(j)
                generate(j + 1, curr)
                # backtrack
                curr.pop()

        generate(1,[])
        return res
