class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we have n cars traveling to the same destination on one lane highway

        res = []
        cars = list(zip(position,speed))
        cars.sort(reverse=True) #sort the cars by position
       

        stack = []

        # iterate through the car and speed
        for pos,speed in cars:
            # print(stack,res)
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # merge them
                stack.pop()
        return len(stack)

