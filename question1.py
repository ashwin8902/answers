import re
 
def isValid(s):
     

    Pattern = re.compile("^\+?\d.\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    return Pattern.match(s)
 
# Driver Code
s = input("enter the number:")

if (isValid(s)):
    print ("Valid Number")    
else :
    print ("Invalid Number")