#############################################################################
## 									   ##
##	Title : Simple Multiplication					   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# Multiply a number by 8 if even else by 9 if odd.

def simple_nulti(num):
	return num * 8 if num % 2 == 0 else num * 9
	
# A clever soln was return n * (8 + n % 2)

# The idea with the above is that when a number is even when you divide it by 2 it will return 0 else if it is odd it will return 1.
