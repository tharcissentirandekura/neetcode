class Solution:
    def trap(self, height: List[int]) -> int:

        l,r = 0, len(height) - 1
        maxleft = height[l]
        maxright = height[r]
        res = 0
        while l < r:
            # get the first index start
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft,height[l])
                water = maxleft - height[l]
                res += water
            else:
                # move from right 
                r -= 1
                maxright = max(maxright,height[r])
                water = maxright - height[r]
                res += water
        return res

        