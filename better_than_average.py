#############################################################################
## 									   ##
##	Title : Better Than Average					   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# Looking for the average in a list and compare it with my points.

def better_than_ave(class_points,my_points):
	ave = sum(class_points)/len(class_points) # Find the Average
	if ave <= my_points:			  # Compare it
		return True
	else:
		return False

'''
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# This quite a really clever way.
'''
