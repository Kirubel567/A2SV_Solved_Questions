class Node: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.start = 0
        self.end = 0


    def visit(self, url: str) -> None:
        #create a node 
        added_node = Node(url)
        self.start += 1

        
        self.head.next = None
        self.end = 0

        #now connect the head to the new added_node 
        self.head.next = added_node 
        added_node.prev = self.head 
        self.head = added_node #make the head pointer to the current node

    def back(self, steps: int) -> str:
        #for this you have to use the self.start to move back 
        move = self.start if steps > self.start else steps

        while move: 
            self.head = self.head.prev
            move -= 1
            self.end += 1
            self.start -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        move = self.end if steps>self.end else steps 

        while move: 
            self.head = self.head.next
            move -= 1
            self.end -= 1
            self.start += 1
        return self.head.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)