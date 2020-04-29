#!/usr/bin/env python3
import re
from parameters import Parameters
from generators import *
import compare_params



def main():
	
	count = 0 #count is a variable that stores count of how many 8bit tails of binary strings matched.
	parameterList = [65, 8921] #say the parameters are fetched from some database and we store them in temporary variables

	for number in parameterList:
		x = re.findall("^[0-9]+$", str(number)) #using regular expression to check if the values passed on to the generators are numbers.
		if x:
			pass
		else:
			print("there was an error with element number", parameterList.index(number)+1, "in the list.")

	First = Parameters(parameterList[0]) #using Parameters class from parameters.py, initiating parameters
	Second = Parameters(parameterList[1])

	
	for x in range(1000000): #where the actual task happens

		First = Parameters(generator_A(Parameters.getParameter(First))) # generators create new values in generators.py and these values replace old values
		Second = Parameters(generator_B(Parameters.getParameter(Second)))
		
		if compare_params.compare('{:032b}'.format(Parameters.getParameter(First)), #Converting new generated values into 32 bit binary and comparing them in compare_params.py
			'{:032b}'.format(Parameters.getParameter(Second))):
			count = count + 1 #Method returns True if strings match, else returns False.

	
	print(count) #final answer


if __name__ == '__main__':
    main()