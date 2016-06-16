def ReplaceString(string):
    charlist=[]
    for char in string:
        if char ==" ":
            char = "%20"
        charlist.append(char)
    return "".join(charlist)


print ReplaceString("i am  ree")


    

            
        
    
