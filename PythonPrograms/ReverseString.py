#reverse a string
class reverseString:

    def rev(self,str):
        self.l = list(str.split())
        print self.l[::-1]
    def revStr(self,str):
        print str[::-1]
        
    

s = reverseString()
s.rev("reena is happy")
s.revStr("reena")

#output:['happy', 'is', 'reena']
#output:aneer


            
        
