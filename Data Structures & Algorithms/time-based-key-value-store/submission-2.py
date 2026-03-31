class TimeMap:

    def __init__(self):
        # here
        self.map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        # take a key
        # value will be a list and the list will be pf (value,timestamp)
        # {alice:[(happy,1),(sad,2)],...(confused,100)}
        # we want to see if the key is already in self.map
        #   if so, I just add values
        #  otherwise I add key with empty list
        if key in self.map: # does the key exist
           self.map[key].append((value,timestamp))
        else:
            self.map[key] = [] # initialize key with empty list
            self.map[key].append((value,timestamp))
        print(self.map)
    def get(self, key: str, timestamp: int) -> str:

        # if key doesn't exist: return false
        if key not in self.map:
            return ""
        # get the list value
        values = self.map.get(key,[])

        # us ebinary search
        # this is a linear search which is O(n)
        # we can use binary search
        # it the time stamp doesn't exist
        # we just return the value at the pointer - 1: previous
        # for value in values:
        #     print(value)
        #     if timestamp == value[1]:
        #         return value[0]
        res = "" #store the result
        l,r = 0, len(values) - 1

        while l <= r:
            mid = (l + r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


