class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # current area is limitted by shortest bar
        # so use two pointer
        #  and take height[right] and height[left]
        # calculate the area using those
        #  decreate the side with lower height
        # if they are equal, do both or any of those

        # The key here is to know when to decrement and increment
        
        l,r = 0,len(heights) - 1

        max_water = -1
        while l <= r:
            distance = r - l
            min_h = min(heights[r],heights[l])
            area = min_h * distance
            print(area)
            if area > max_water:
                max_water = area
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_water
            

