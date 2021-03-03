def multiply(num1, num2):

	primitives = 0
	addends = []

	num2_coefficient = 1

	for digit2 in reversed(list(num2)):
		num1_coefficient = 1
		#print(f'num2_coefficient = {num2_coefficient}')
		for digit1 in reversed(list(num1)):
			#print(f'num1_coefficient = {num1_coefficient}')
			factor2 = int(digit2) * num2_coefficient
			factor1 = int(digit1) * num1_coefficient
			product = factor1 * factor2
			#print(f'{factor1} x {factor2} = {product}')
			primitives += 1
			addends.append(product)
			num1_coefficient = num1_coefficient * 10
		num2_coefficient = num2_coefficient * 10
		#print()


	sum = 0
	
	for addend in addends:
		sum += addend
	
	primitives += len(addends)-1

	return sum, primitives

print(multiply('12345678', '12345678'))