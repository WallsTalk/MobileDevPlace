def compare(first_parameter, second_parameter):
	#compares lat 8 bits of parameter values in binary and returns true or false.
	if first_parameter[-8:] == second_parameter[-8:]:
		return True
	else:
		return False