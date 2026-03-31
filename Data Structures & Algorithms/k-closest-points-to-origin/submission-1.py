class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  calculate the distance from the origin and store it in the max heap
        # if done, return the first kth elements
        heap = []
        # calculate the distance
        for  point in points:
            dist = ((point[0] - 0)**2 + (point[1] - 0) **2) ** 0.5
            heapq.heappush(heap, (dist,point))

        res = []

        for i in range(k):
            closest = heapq.heappop(heap)
            res.append(closest[1])
        
        return res




