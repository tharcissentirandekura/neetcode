class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashset = {}
        result = []
        for num in nums:
            if num not in Hashset:
                Hashset[num] = 1
            else:
                Hashset[num] += 1
        

        
        sorted_items = sorted(Hashset.items(), key=lambda item: item[1],reverse=True)
        temp = {k: v for k, v in sorted_items}
        return list(temp.keys())[:k]
        
        