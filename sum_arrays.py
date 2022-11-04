#############################################################################
## 									   ##
##	Title : Sum Arrays						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################


# Basically look for the sum of an array and it should return 0 if array is [].

def sum_array(a):
    b = []
    if a == b:
        return 0
    else: 
        return sum(a)
        
# 1 Thing I didnt realise was an empty array would return 0 if sum is done.
# Some of the clever ways I saw.
# 	return sum(a) if a !=0 else 0

#	return sum(a)


