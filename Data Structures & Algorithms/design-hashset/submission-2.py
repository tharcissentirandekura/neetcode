class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
    def hash(self,key):
        return key % self.size
    def add(self, key: int) -> None:
        # get the hash
        index = self.hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        # get the index
        index = self.hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return key in self.table[index] 

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)