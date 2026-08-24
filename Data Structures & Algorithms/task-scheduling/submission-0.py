class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        table = {}
        for task in tasks:
            table[task] = table.get(task,0) + 1

        heap = []
        for task,freq in table.items():
            heapq.heappush(heap,(-freq,task))

        count = 0
        # res = []
        while heap:
            prev = []
            used = 0
            for i in range(n + 1):
                # print(res, heap,prev)
                if heap:
                    freq,task = heapq.heappop(heap)
                    # res.append(task)
                    freq += 1
                    used += 1
                    if freq < 0:
                        prev.append((freq,task))
                # else:
                #     # tasks waiting in idle
                #     if prev:
                #         res.append("Idle")

            for item in prev:
                heapq.heappush(heap,item)
            if heap:
                count += n + 1
            else:
                count += used
        # print(res)
        return count
