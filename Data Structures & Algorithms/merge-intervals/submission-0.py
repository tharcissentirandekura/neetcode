class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        for interval in intervals:
            start,end = interval[0], interval[1]

            if not merged or start > merged[-1][1]:
                merged.append([start,end]) # no overlap
            else:
                # overlap: so extend
                merged[-1][1] = max(merged[-1][1], end)
        return merged
        