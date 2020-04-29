def compare_A(first_parameter, second_parameter):
	#compares lat 8 bits of parameter values in binary and returns true or false.
	if '{:032b}'.format(first_parameter)[-8:] == '{:032b}'.format(second_parameter)[-8:]:
		return True
	else:
		return False