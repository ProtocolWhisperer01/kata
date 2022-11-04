#############################################################################
## 									   ##
##	Title : 							   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# In this I'm supposed to count the number of odd numbers below a give number n.

def odd_count(n):
	count = 0
	for i in range(1, n):
		if i % 2 != 0:
			count += 1 
		else: 
			continue	
	return count

# So with the above i got the count quite easily for a smaller range however a bigger range is quite interesting, ie i got a time out error.
# After search the interwebs the actual work aroun was to use floored division which is quite clever, coz think about it.
'''
	if n is 21 and you do 21//2 you will get 10 and 10 in turn is the count.
	The theory is that you have to step 1 to get to an odd number so having n gives an equal number of odd numbers and even numbers.
	
'''
def odd_num_count(n):
	return n // 2
	return len(range(1,n,2)) # this is also a honorable mention.
