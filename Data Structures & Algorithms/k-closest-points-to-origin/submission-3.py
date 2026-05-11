class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  calculate the distance from the origin and store it in the max heap
        # if done, return the first kth elements
        heap = []
        # calculate the distance
        for  x,y in points:
            dist = ((x - 0)**2 + (y - 0) **2)
            heapq.heappush(heap, (dist,[x,y]))

        res = []

        for i in range(k):
            closest = heapq.heappop(heap)
            res.append(closest[1])
        
        return res




