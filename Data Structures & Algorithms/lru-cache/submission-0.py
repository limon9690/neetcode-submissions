class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.store = {}


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self.delete_node(node)
        self.add_to_tail(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            self.delete_node(node)
            
            node.val = value
            self.store[key] = node
            self.add_to_tail(node)
            return

        node = Node(key, value)
        if len(self.store) < self.capacity:
            self.store[key] = node
            self.add_to_tail(node)
        else:
            lru = self.head.next
            self.delete_from_head()
            del self.store[lru.key]
            self.store[key] = node
            self.add_to_tail(node)


    def delete_node(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt
        node.next = None
        node.prev = None


    def add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


    def delete_from_head(self):
        node = self.head.next
        nxt = node.next
        self.head.next = nxt
        nxt.prev = self.head
        node.next = None
        node.prev = None
        
