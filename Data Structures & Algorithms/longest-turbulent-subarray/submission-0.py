class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        up = 1
        down = 1

        res = 1

        for i in range(1,len(arr)):
            if arr[i] > arr[i - 1]:
                # flip
                up = down + 1 # the longest turb sub ending at i with last down flip
                down = 1
            elif arr[i] < arr[i - 1]:
                # now the longest turb sub ending at i has latest up flip sign
                down = up + 1
                up = 1
            else:
                # same numbers
                # reset
                up = down = 1
            res = max(res,up,down)
        return res

