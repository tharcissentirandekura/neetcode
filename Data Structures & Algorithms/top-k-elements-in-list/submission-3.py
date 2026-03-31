class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # fill in the lists equal to number of elements
        freq = [[] for i in range(len(nums)+1)]
        # get the num and its count
        for num in nums:
            count[num] = 1 + count.get(num,0)
        # populate the array with value in its count, value with
        # low count will be in front
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        #go in list in reverse as higher count value are in back
        # in each each bucket, append the values
        # if values are equal to k, return its list
        for i in range(len(freq) - 1, 0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
        