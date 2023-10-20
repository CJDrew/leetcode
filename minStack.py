class MinStack:
    class ListNode:
       def __init__(self, val):
           self.val = val
           self.next = None

    def __init__(self):
        self.root = ListNode(0)
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        cur = ListNode(val)

        if val < self.min:
            self.min = val

        cur.next = self.root.next
        self.root.next = cur

    def pop(self) -> None:
        if self.root.next:
            cur = self.root.next
            self.root.next = self.root.next.next
            return cur.val
        return None

    def top(self) -> int:
        if self.root.next:
            return self.root.next.val
        return None

    def getMin(self) -> int:
        if not self.root.next:
            return None
        return self.min


test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)