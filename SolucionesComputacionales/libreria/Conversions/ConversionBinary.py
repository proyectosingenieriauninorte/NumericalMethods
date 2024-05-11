def binary_to_decimal(valor):
    """
    Converts a binary string to its decimal equivalent.
    
    Args:
        valor (str): Binary string representing the number (integer or floating-point).
        
    Returns:
        float: Decimal equivalent of the binary number represented by valor.
    """
    if "." not in valor:
        posicion = 0
        decimal = 0
        valor = valor[::-1]
        for digito in valor:
            multiplicador = 2 ** posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal
    else:
        entera, fraccionaria = valor.split(".")
        
        cant_entera = len(entera)
        posicion = 0
        decimal = 0
        entera = entera[::-1]
        for digito in entera:
            multiplicador = 2 ** posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        
        posicion1 = 1
        decimal1 = 0
        fraccionaria = fraccionaria[::-1]
        for digito in fraccionaria:
            multiplicador1 = 2 ** -posicion1
            decimal1 += int(digito) * multiplicador1
            posicion1 += 1
        
        res = decimal + decimal1
        return res


"""
#Example:
binary_number = "1101.101"  
decimal_value = binary_to_decimal(binary_number)
print("Decimal equivalent:", decimal_value)
"""

