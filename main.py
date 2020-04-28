#!/usr/bin/env python3
from parameters import parameters
import generators
import compare_params




def main():
	#count is a variable that stores count of how many 8bit tails of binary strings matched.
	count = 0
	
	for x in range(1000000):
		'''
		Using generators with starting parameters imported from paramters class located in parameters.py and
		fetching generated values from generators (generators are located in generators.py).
		'''
		parameters.First = generators.generator_A(parameters.First)
		parameters.Second = generators.generator_B(parameters.Second)

		'''
		Converting new generated values into 32 bit binary like shown in the task 
		using method compare to compare them.
		Method returns True if strings match, else returns False.
		'''
		if compare_params.compare('{:032b}'.format(parameters.First), '{:032b}'.format(parameters.Second)):
			count = count + 1

	print(count)

if __name__ == '__main__':
    main()