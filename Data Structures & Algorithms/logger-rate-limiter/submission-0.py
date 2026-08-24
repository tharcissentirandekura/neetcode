from collections import deque
class Logger:

    def __init__(self):
        self.logMap = {}
        self.waitingLogs = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logMap:
            # add it and print it
            self.logMap[message] = timestamp + 10
            return True
        else:
            # check if should print
            nextAllowedPrint = self.logMap[message]
            if  timestamp >= nextAllowedPrint:
                # shouldprint = true
                self.logMap[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
