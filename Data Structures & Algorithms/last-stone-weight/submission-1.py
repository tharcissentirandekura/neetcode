class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # insert all elememts in the heap and pick the top 2 smash them and remove the smallest and replace biggest with resu

        stones = [-s for s in stones]
        heapq.heapify(stones) # add all elements in the heap

        while len(stones) > 1:
            first,second = heapq.heappop(stones),heapq.heappop(stones)

            # diff
            if second > first:
                # first is destroyed
                heapq.heappush(stones, first - second)
        # all are destoyed
        stones.append(0)

        return abs(stones[0]) #top of the heap




