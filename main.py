#!/usr/bin/env python3
from parameters import Parameters
import generators
import compare_params


def main():
	#count is a variable that stores count of how many 8bit tails of binary strings matched.
	count = 0

	'''
	x = re.findall("Portugal", txt)
	print(x)
	'''

	#using Parameters class from parameters.py, initiating parameters
	First = Parameters(635)
	Second = Parameters(12)

	for x in range(1000000):
		pass
		'''
		Using generators with starting parameters creating new parameters 
		and storing new vlues into previously initiated parameters
		'''

		First = Parameters(generators.generator_A(Parameters.getParameter(First)))
		Second = Parameters(generators.generator_B(Parameters.getParameter(Second)))

		'''
		Converting new generated values into 32 bit binary like shown in the task 
		using method compare to compare them.
		Method returns True if strings match, else returns False.
		'''
		if compare_params.compare('{:032b}'.format(Parameters.getParameter(First)),'{:032b}'.format(Parameters.getParameter(Second))):
			count = count + 1

	print(count)

if __name__ == '__main__':
    main()