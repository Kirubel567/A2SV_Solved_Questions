class Node: 
    def __init__(self, val): 
        self.val = val
        self.next = None
        self.prev = None
    
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head:
            self.head = Node(value)
            self.tail = self.head 
        else:
            added = Node(value)
            added.next = self.head
            self.head.prev = added 
            self.head = added
        self.count+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head:
            self.tail = Node(value)
            self.head = self.tail 
        else:
            added = Node(value)
            added.prev = self.tail
            self.tail.next = added 
            self.tail = added
        self.count+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): 
            return False 
        if self.head == self.tail: 
            self.head = self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return True 

    def deleteLast(self) -> bool:
        if self.isEmpty(): 
            return False
        if self.head == self.tail: 
            self.head = self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None

        self.count-=1
        return True 

    def getFront(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return True if not self.head else False

    def isFull(self) -> bool:
        return True if self.count == self.k else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()