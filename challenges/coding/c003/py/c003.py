import os
import re


def solve(s):
    s = re.sub(' +', ' ', s)
    
    words = s.split(" ")
    
    upper_words = [word.capitaliza() for word in words]
   
    full_name = ' '.join(upper_words)
    
    return(full_name)        
    
    
if __name__ == '__main__':
    
    s = "randolfo     edecio castillo acosta"
    result = solve(s)
    
    print(result)