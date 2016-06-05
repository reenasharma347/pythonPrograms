class Node(object):
    def __init__(self,data=None,node_next=None):
        self.data = data
        self.node_next =node_next

    def get_data(self):
        return self.data
    def get_next(self):
        return self.node_next
    def set_next(self,new_next):
        self.node_next=new_next
            
class LinkedList(object):
    def __init__(self,head=None):
        self.head =head

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        print "inserted"
    def size(self):
        current_node =self.head
        count=0
        while current_node:
            count+=1
            current_node = current_node.get_next()
        return count
    def search(self,data):
        current_node=self.head
        found=False
        print "trace1"
        while current_node and found is False:
            print "Trace2"
            if current_node.get_data()==data:
                found = True
                print 'found',data
            else:
                current_node = current_node.get_next()
                print "trcae 3"
        if current_node is None:
            raise ValueError("data does not exist")
        return current_node

    def remove(self,data):
        current_node=self.head
        found =False
        previous = None
        while current_node and found is False:
            if current_node.get_data == data:
                found = True
                print 'found to remove'
            else:
                previous = current_node
                current_node= current_node.get_next()
            if current_node is None:
                raise ValueError("data does not exists")
            if previous is None:
                self.head = current_node.get_next()
            else:
                previous.set_next(current_node.get_next())

a =LinkedList();
a.insert(16)
a.search(16)

