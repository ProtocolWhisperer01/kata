#############################################################################
## 									   ##
##	Title : Math Floor.py						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################


# This an easy computation of rounding off to the smallest value.

from math import floor

def liters(time): # Time is in hours
	return floor(0.5 * time)

# Clever ways that I saw was using floored division //  also have the int() type will also lead to a floored result.
