from LinkedList import *
class duplicate:
    #hashmap complexity o(n)
    def removeDuplicate(linkedlist):
        if linkedlist.head !=None:
            current = linkedlist.head
            dic ={current.value:True}
            while current.next !=None:
                if current.next.value in dic:
                    current.next = current.next.next
                    
                else:
                    dic[current.next.value]=True
                    current= current.next
                    
    #without using buffer O(n2)

    def deleteDuplicate(linkedlist):
        if linkedlist.head != none:
            current= linkedlist.head
            
            while current.next !=None:
                p1 = current
                while p1.next !=None:
                    if p1.next.value ==current.value:
                       p1.next =p1.next.next

                    else:
                        p1 =p1.next
                current = current.next
                        
                
            
        
        
