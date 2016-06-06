class QueueLinear:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def showQueue(self):
        for i in self.items:
            print i,

q =QueueLinear()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.showQueue()
            
        
