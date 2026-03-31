class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # number of days after ith day before it gets warmer
        # we keep counting until temp[i] > temp[jth]
        # quadratic, go thought temp and compare the rest

        # quadratic polynomials time

        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = (j - i)
        #             break
        # return res

        """ 
            Instead of using two nested loops, we can use stack
            next smallest elemensts:

            how long it takes to arrive to a bigger number
            stack: keeps track of days that are still waiting for warmer
        
        """

        # linear time
        stack = [0]
        
        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = (i - j)
            stack.append(i)
        return res
 



