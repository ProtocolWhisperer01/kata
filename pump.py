
#############################################################################
## 									   ##
##	Title : Pump							   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# This was a simple arithmetic equation. just doing simple comparison

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False


# A clever way I could have done this was:
# return distance_to_pump <= mpg * fuel_left since it is comparing it would have led to a bool response. 
