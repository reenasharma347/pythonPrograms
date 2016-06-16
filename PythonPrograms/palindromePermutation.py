def palindromePermutation(string):
    charList =list(string)
    count_char =[charList.count(x) for x in set(charList)]
    mid_char =[x for x in count_char if x%2==1]
    if len(mid_char)==0 or len(mid_char)==1:
        return True
    else:
        return False

print palindromePermutation("aabb")            
                
        
        
