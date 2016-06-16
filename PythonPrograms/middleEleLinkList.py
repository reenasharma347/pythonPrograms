class Node:
    def __init__(self,data=None,node_next=None):
        self.data =data
        self.node_next=node_next
    def __str__(self):
        return str(self.data)

    def createList(self,n):
        link_list = Node(1)
        Head = link_list
        for i in range(2,n):
            Head.node_next = Node(i)
            Head = Head.node_next
        return link_list

    def print_list(self,node):
        while (node):
            print '[',node,']','[ref] ->',
            node =node.node_next
        print '-> None'

    def findMiddle(self,node):
        flag = False
        half = node
        while node:
            node = node.node_next
            if flag:
                half =half.node_next
            flag = not flag
        return "middle ele is %s" % str(half)



a=Node()
node =a.createList(5)
print a.createList(5)
print a.print_list(node)
print a.findMiddle(node)

            


    
            
            
        
        
