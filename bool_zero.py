#############################################################################
## 									   ##
##	Title : Zero False Other True					   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# In this kata basically brought into play about the boolean type.

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love. 
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def love(f1,f2):
	return True if (f1 % 2 == 0 and f2 % 2 != 0) or (f1 % 2 != 0 and f2 % 2 == 0) else False
	

# A clever way was basically return (f1+f2) % 2 

# So whether both f1 and f2 are equal or both are odd which when a modulous of 2 is done it should return 0 which is false 

# Ie True is 1/ON False is 0/OFF
