class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # number of days after ith day before it gets warmer
        # we keep counting until temp[i] > temp[jth]
        # quadratic, go thought temp and compare the rest
        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1,len(temperatures)):
                print(temperatures[i],":",temperatures[j])
                count = 0
                if temperatures[i] < temperatures[j]:
                    res[i] = (j - i)
                    break
                
                
        return res



