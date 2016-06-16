# three edits insert,remove,replace
def edits(str1,str2):
    #case1 replace
    l1=list(str1)
    l2=list(str2)
    
    if (len(str1)==len(str2))and set(l1)==set(l2):
        print"1"
        return False
    elif (len(str1)==len(str2)) and (len(set(l1)-set(l2))==1 or len(set(l2)-set(l1))==1):
        print "2"
        return True
    elif(len(str1)!=len(str2)) and (len(set(l1)-set(l2))==1 or len(set(l2)-set(l1))==1):
        print "3"
        return True
    else:
        print "4"
        return False
    
print edits("pale","pale")
        
        
