class Node:
    def __init__(self, key: int, value: int):
        #Each node willl store a key-value pair and pointers to prev and next nodes
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        #initialize cache with a given capacity
        self.capacity = capacity
        #we will use a dictionary to store key -> node for O(1) access
        self.cache = {}

        #we will create two dummy nodes: left (least recently used) and right (most recently used)
        self.left = Node(0,0)
        self.right = Node(0,0)

        #connect two dummy nodes together
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        #first, let's chech if the key exists in the cache
        if key in self.cache:
            node = self.cache[key]
            #if it exists, we move it to the right (most recently used)
            self._remove(node)
            self._insert_to_right(node)
            return node.value
            #if not found return -1
        return -1

        

    def put(self, key: int, value: int) -> None:
        #If the key already exists, remove the old node
        if key in self.cache:
            self._remove(self.cache[key])

        #Create a new node and add it to the cache and to the right end
        node = Node(key, value)
        self.cache[key] = node
        self._insert_to_right(node)

        #If we've exceeded the capacity, we remove the least recently used item
        if len(self.cache) > self.capacity:
            # The LRU node is right after the left dummy node
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        
    def _remove(self, node: Node):
        # This helper function removes a node from the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_to_right(self, node: Node):
        # his helper function inserts a node right before the right dummy node
        #So, it becomes the most recently used node
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
