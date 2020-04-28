from coefficients import coefficients

'''
Standart values generated during division are in precision of Double - 64 bit (15-16 digits)
In case better precision is needed it can be changed.
'''

def generator_A(parameter):
	#Takes parameter and usses coefficient A	
	generated_value = parameter*coefficients.A%2147483647
	return generated_value


def generator_B(parameter):
	#takes parameter and uses coefficient B
	generated_value = parameter*coefficients.B%2147483647
	return generated_value

print("Generators loaded.")