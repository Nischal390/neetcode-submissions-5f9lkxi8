class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_cap = capacity
        self.lru_cache = {}
        self.cap = 0
        self.cache_head = None
        self.cache_tail = None

        
    def remove(self, node):
        if node == self.cache_head and node == self.cache_tail:
            self.cache_head = self.cache_tail = None

        elif node == self.cache_head:
            self.cache_head = node.prev
            self.cache_head.next = None
   
        elif node == self.cache_tail:
            self.cache_tail = self.cache_tail.next
            self.cache_tail.prev = None
  
        else:
            node_before = node.prev
            node_after = node.next

            node_before.next = node_after
            node_after.prev = node_before

        node.next = node.prev = None

        return node

    def add(self, node):
        if self.cache_head == None:
            self.cache_head = self.cache_tail = node
            return node
        self.cache_head.next = node
        node.prev = self.cache_head
        self.cache_head = node
        return node

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            node = self.remove(self.lru_cache[key])
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            node = self.remove(self.lru_cache[key])
            node.val = value
            self.add(node)
            self.lru_cache[key] = node
            return
        elif self.cap==self.max_cap:
            _ = self.remove(self.cache_tail)
            del self.lru_cache[_.key]
            node = Node(key, value)
            node = self.add(node)
            self.lru_cache[key] = node
            return
        else:
            node = Node(key, value)
            node = self.add(node)
            self.lru_cache[key] = node
            self.cap+=1