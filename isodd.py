class IsoddError(Exception): pass  
class TypeError(IsoddError):pass

def isOdd(n):
    if type(n)==int :
         if n%2 != 0 : 
             return n
         else: 
             return n+1 	
    else:	
        raise TypeError,"Invalid"

