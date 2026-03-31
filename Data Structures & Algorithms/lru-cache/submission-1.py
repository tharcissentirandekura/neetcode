class ListNode:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # each k is ListNode
        self.capacity = capacity

        # create dummry head and tail
        self.head = ListNode()
        self.tail  = ListNode()

        # connect
        self.head.next = self.tail
        self.tail.prev = self.head
    def remove_node(self,node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
    def add_tail(self,node):
        last = self.tail.prev
        last.next = node
        node.prev =last
        node.next = self.tail
        self.tail.prev = node
    def move_to_tail(self,node):
        self.remove_node(node)
        self.add_tail(node)
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # move it to end and return it
            node = self.cache[key]
            self.move_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update and move it to end
            node = self.cache[key]
            node.value = value
            self.move_to_tail(node)
        else:
            # add new
            new_node = ListNode(key,value)
            self.cache[key] = new_node
            self.add_tail(new_node)

            # evict if over
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self.remove_node(lru_node)
                self.cache.pop(lru_node.key)