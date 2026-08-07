class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _insert(self,node:Node):
        prev,nxt = self.right.prev,self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    
    def _remove(self,node:Node):
        prev,nxt = node.prev , node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        new_node = Node(key,value)
        self.cache[key] = new_node
        self._insert(new_node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


class Node:
    
    def __init__(self,key : int = 0, val : int = 0):
         self.val = val
         self.key = key
         self.prev = None
         self.next = None
        


        
