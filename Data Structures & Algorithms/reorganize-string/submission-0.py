class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap = {}
        heap = []
        for char in s:
            countMap[char] = countMap.get(char,0) + 1

        # add all values in the heap
        for char,count in countMap.items():
            heapq.heappush(heap,(-count,char))
        
        res = []
        prev_char = ""
        prev_freq = 0
        
        while heap:
            freq,char = heapq.heappop(heap)
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq,prev_char))
    
            freq += 1
            prev_freq = freq
            prev_char = char

        if len(res) != len(s):
            return ""
                
    
        return "".join(res)