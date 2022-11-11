#############################################################################
## 									   ##
##	Title : Multiplication Of Items in a list			   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################


# In this, I was being tested of items in a list and getting a positive difference.

from numpy import prod
def find_difference(a, b):
    return prod(a) - prod(b) if prod(a) > prod(b) else prod(b) - prod(a)
    
