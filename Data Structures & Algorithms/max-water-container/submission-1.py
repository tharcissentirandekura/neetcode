class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # current area is limitted by shortest bar
        # so use two pointer
        #  and take height[right] and height[left]
        # calculate the area using those
        #  decreate the side with lower height
        # if they are equal, do both or any of those

        # The key here is to know when to decrement and increment
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            # get the area
            area = min(heights[l],heights[r]) * (r - l)
            res = max(res,area)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -=1
        return res
            

