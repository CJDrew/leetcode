class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.front = ListNode(0, 0)
        self.back = ListNode(0, 0)
        self.front.next = self.back
        self.back.prev = self.front      

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes.get(key)
        self._removeNode(node)
        self._addNodeToFront(node)
        return node.val     

    def put(self, key: int, value: int) -> None: 
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._removeNode(node)
            self._addNodeToFront(node)
        else:
            node = ListNode(key, value)
            self.nodes[key] = node
            self._addNodeToFront(node)
            if len(self.nodes) > self.capacity:
                self.nodes.pop(self.back.prev.key)
                self._removeNode(self.back.prev)

    
    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _addNodeToFront(self, node):
        node.next = self.front.next
        node.prev = self.front
        self.front.next.prev = node
        self.front.next = node

test = LRUCache(2)
test.put(1, 1)
test.put(2, 2)
print(test.get(1))
test.put(3, 3)
print(test.get(2))
test.put(4, 4)
print(test.get(1))
print(test.get(3))
print(test.get(4))
