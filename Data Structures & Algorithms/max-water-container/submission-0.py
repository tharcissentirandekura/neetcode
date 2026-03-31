class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # current area is limitted by shortest bar
        # so use two pointer
        #  and take height[right] and height[left]
        # calculate the area using those
        #  decreate the side with lower height
        # if they are equal, do both or any of those


        l,r = 0, len(heights) - 1
        area = 0
        while l < r:
            # get the area
            width = r - l
            height = min(heights[l],heights[r])
            if area < width * height:
                area = width * height
            if heights[r] > heights[l]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return area
            

