class stackArr:
    def __init__(self):
        self.items =[]
        self.item=None
        print "init"
    def push(self,data):
        self.items.append(data)
    def peek(self):
        if len(self.items)==0:
            raise ValueError("list is empty")
        else:
            return self.items[len(self.items)-1]
    def pop(self):
        if len(self.items)==0:
            raise ValueError("list is empty ")
        else:
            self.item = self.items[len(self.items)-1]
            del self.items[len(self.items)-1]
    def isEmpty(self):
        
        return len(self.items)==0
        
            
        

a=stackArr()
a.push(2)
print a.peek()
print a.isEmpty()


            
        
         
