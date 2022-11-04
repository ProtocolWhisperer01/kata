#############################################################################
## 									   ##
##	Title :  Power Array						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################


# This was a simple one, loop through a given range and have each value power 2, the result should be resulted in form of a list.

num_list = []
for i in range(n+1):
	x = 2 ** i
	num_list.append(x)
return num_list

# A clever way I saw was:
#	return [2**i for i in range(n+1)]
