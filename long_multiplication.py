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
    
    n1 = len(num1)
    print(f'n1 = {n1}')
    
    n2 = len(num2)
    print(f'n2 = {n2}')
    
    prod_n = n1 * n2
    print(f'2ProdN = {prod_n * 2}')
    print(f'Product = {sum}')
    print(f'Primitives = {primitives}')
    x = n1 * n1 * 2
    print(f'2n1^2 = {x}')
    y = n2 * n2 * 2
    print(f'2n2^2 = {y}')
    p = primitives + 1



multiply('123456', '12')