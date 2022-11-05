#############################################################################
## 									   ##
##	Title : 							   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# In this kata I had to make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def catch_exc(a):
	return a * 50 + 6 if isinstance(a,int) or isinstance(a,float) else  "Error"
	

# the catch was basically being able to catch the type() of each value.
# isstance() was quite a help. It check if an object is of a particular type with the built-in function as shown above.
# the easiest way I could have written the above is returning the 'error' if the instance is string else do the math. 
