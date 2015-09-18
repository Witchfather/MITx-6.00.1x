def sharp(x):
    '''
    (int) -> int
    x: the number to calculate sharp

    Returns the sharp of x, calculating the powers of 2 through x recursively.
    Sharp of x can be defined as (((((2 ** 3) ** 4) ** 5) ... ** x-1) ** x).
    '''
    if x < 2:
        return 0
    if x == 2:
        return x

    return sharp(x - 1) ** x

def ndigits(x):
    '''
    (int) -> int
    x: the number to calculate number of digits

    Returns the number of digits of x.
    '''
    if abs(x) < 10:
        return 1

    digs = 1
    return digs + ndigits(x / 10)

#result = ndigits(sharp(7)) + 2 * ndigits(sharp(6)) + ndigits(sharp(5)) + ndigits(sharp(4))
#print result
