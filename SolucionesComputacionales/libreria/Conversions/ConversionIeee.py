
def ieee754(N):
    """
    Converts a binary string representing a number in IEEE-754 floating-point format to its decimal equivalent.
    Args:
        N (str): Binary string representing the IEEE-754 floating-point number.
    Returns:
        float: Decimal equivalent of the IEEE-754 floating-point number represented by N.
    """
    a = int(N[0])
    b = int(N[1:9], 2)
    c = int(N[9:], 2)

    exponent_bias = 127
    denominator = 1 << (len(N) - 9)

    if b == 0 and c == 0:
        return 0.0
    elif b == 255 and c == 0:
        return float('-inf') if a == 0 else float('inf')
    elif b == 255 and c != 0:
        return float('nan')
    else:
        return (-1)**a * (1 + c / denominator) * 2 **(b - exponent_bias)

    """
    #Example:
    N = "01111110010000111110100100100010"
    print(ieee745(N))
    """