#############################################################################
## 									   ##
##	Title : Reverse a  List 		 			   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
	num_list = [] #1. Decided to create an empty list.
	
	# The idea is to loop through the give range in n; the range should start from 1 all the way to n
	# with the range fun however it usually never outputs the last expected digit, so I added 1 to n.

	for i in range(1, n + 1):
		num_list.append(i) # For each iteration/loop add a number to the list.
	num_list.reverse() # Now reverse the list last #no to be first and first to be last.
	return num_list


'''
A clever that i saw when reviewing was using:
	range(10,0,-1)
	
	Basically the you are starting from 10 till 1 but not to 0 and in that way you will have to decrement by 1, hence the step -1.
	
'''
