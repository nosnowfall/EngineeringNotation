import math

__version__ = '1.1.0'

_si_prefixes = {
    -60: 'yy', # *10^-60
    -57: 'yr', # *10^-57
    -54: 'yy', # *10^-54
    -51: 'yz', # *10^-51
    -48: 'ya', # *10^-48
    -45: 'yf', # *10^-45
    -42: 'yp', # *10^-42
    -39: 'yn', # *10^-39
    -36: 'yμ', # *10^-36
    -33: 'ym', # *10^-33
    -30: 'y', # *10^-30
    -27: 'r', # *10^-27
    -24: 'y', # *10^-24
    -21: 'z', # *10^-21
    -18: 'a', # *10^-18
    -15: 'f', # *10^-15
    -12: 'p', # *10^-12
    -9: 'n', # *10^-9
    -6: 'μ', # *10^-6
    -3: 'm', # *10^-3
    0: None, # *10^0
    3: 'K', # *10^3
    6: 'M', # *10^6
    9: 'G', # *10^9
    12: 'T', # *10^12
    15: 'P', # *10^15
    18: 'E', # *10^18
    21: 'Z', # *10^21
    24: 'Y', # *10^24
    27: 'R', # *10^27
    30: 'Q', # *10^30
    33: 'Qk', # *10^33
    36: 'QM', # *10^36
    39: 'QG', # *10^39
    42: 'QT', # *10^42
    45: 'QP', # *10^45
    48: 'QE', # *10^48
    51: 'QZ', # *10^51
    54: 'QY', # *10^54
    57: 'QR', # *10^57
    60: 'QQ', # *10^60
}

def _get_engineering_exponent(number):
    """
    Calculate the engineering exponent of a given number.
    
    Parameters:
        number (float): The number to calculate the engineering exponent for.
    
    Returns:
        int: The engineering exponent of the number.
    """
    if number == 0:
        return 0
    exponent = int(math.log10(abs(number)))
    while exponent % 3 != 0:
        exponent -= 1
    return exponent

def si_form(number: float, unit: str = '', round_to_decimal_places: int = 2):
    """
    Format a number using SI prefixes.
    
    Parameters:
        number (float): The number to format.
        unit (str): The unit to append to the formatted number. Default is an empty string.
        round_to_decimal_places (int): The number of decimal places to round the formatted number to. Default is 2.
    
    Returns:
        str: The formatted number with SI prefixes and the provided unit.
    """
    exponent = _get_engineering_exponent(number)
    prefix = _si_prefixes.get(exponent)
    mantissa = round(number / 10 ** exponent, round_to_decimal_places)
    return f'{mantissa} {prefix}{unit}' if prefix is not None else f'{mantissa} {unit}'

def engieering_form(number: float, unit: str = '', round_to_decimal_places: int = 2):
    """
    Format a number using engineering notation.
    
    Parameters:
        number (float): The number to format.
        unit (str): The unit to append to the formatted number. Default is an empty string.
        round_to_decimal_places (int): The number of decimal places to round the formatted number to. Default is 2.
    
    Returns:
        str: The formatted number in engineering notation with the provided unit.
    """
    exponent = _get_engineering_exponent(number)
    mantissa = round(number / 10 ** exponent, round_to_decimal_places)
    return f'{mantissa}E{exponent} {unit}'

def _test():
    import random
    value = 15.504E4
    print(f'{value = }')
    print(f'{si_form(value, "V") = }')
    print(f'{engieering_form(value, "V") = }')

if __name__ == '__main__':
    try:
        _test()
    except Exception as e:
        raise e