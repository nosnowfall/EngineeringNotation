import math

__version__ = '1.2.2'

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
    0: None, # *10^0, None type makes formatting easier
    3: 'k', # *10^3
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

def _get_engineering_exponent(number:float) -> int:
    """
    Calculate the engineering exponent of a given number.
    
    Parameters:
        number (float): The number to calculate the engineering exponent for.
    
    Returns:
        int: The engineering exponent of the number.
    """
    if number == 0:
        exponent = 0
    else:
        exponent = int(math.floor(math.log10(abs(number))/3)*3) # method found in matplotlib/lib/matplotlib/ticker.py EngFormatter.format_data()
    return exponent

def _get_exp_str(exponent:int) -> str:
    """
    Handle printing positive, negative, and zero exponents

    Parameters:
        exponent (int): the exponent to be formatted for engineering notation

    Returns:
        str: formatted exponent, e.g. E+3 or E-2 or ''
    """
    signstr = ''
    if exponent > 0:
        signstr = f'E+{exponent}' # manually add in the + sign
    elif exponent < 0:
        signstr = f'E{exponent}' # negative is included in autoformat
    else:
        signstr = ''
    return signstr

def si_form(number: float, unit: str = '', round_to_decimal_places: int = 2) -> str:
    """
    Format a number using SI prefixes.
    
    Parameters:
        number (float): The number to format.
        unit (str): The unit to append to the formatted number. Default is an empty string.
        round_to_decimal_places (int): The number of decimal places to round the formatted number to. Default is 2.
        if 0 is after the decimal, it is now omitted
        
    Returns:
        str: The formatted number with SI prefixes and the provided unit.
    """
    exponent = _get_engineering_exponent(number)
    prefix = _si_prefixes.get(exponent)
    mantissa = str(round(number / 10 ** exponent, round_to_decimal_places)).rstrip('0').rstrip('.')
    if mantissa in ('-1000','1000'):
        exponent += 3
        mantissa = str(round(number / 10 ** exponent, round_to_decimal_places)).rstrip('0').rstrip('.')
    outstr = f'{mantissa} {prefix}{unit}' if prefix is not None else f'{mantissa} {unit}'
    return outstr.rstrip()

def engineering_form(number: float, unit: str = '', round_to_decimal_places: int = 2) -> str:
    """
    Format a number using engineering notation.
    
    Parameters:
        number (float): The number to format.
        unit (str): The unit to append to the formatted number. Default is an empty string.
        round_to_decimal_places (int): The number of decimal places to round the formatted number to. Default is 2.
        if 0 is after the decimal, it is now omitted

    Returns:
        str: The formatted number in engineering notation with the provided unit.
    """
    exponent = _get_engineering_exponent(number)
    mantissa = str(round(number / 10 ** exponent, round_to_decimal_places)).rstrip('0').rstrip('.')
    if mantissa in ('-1000','1000'):
        exponent += 3
        mantissa = str(round(number / 10 ** exponent, round_to_decimal_places)).rstrip('0').rstrip('.')
    return f'{mantissa}{_get_exp_str(exponent)} {unit}' if unit != '' else f'{mantissa}{_get_exp_str(exponent)}'

# alias functions
def sif(num:float, uni:str = '', prec:int = 2) -> str:
    """
    alias of si_form()
    """
    return si_form(num,unit=uni,round_to_decimal_places=prec)

def engf(num:float, uni:str = '', prec:int = 2) -> str:
    """
    alias of engineering_form()
    """
    return engineering_form(num, unit=uni, round_to_decimal_places=prec)

def _test():
    import random
    value = -999.9E-6
    print(f'{value = }')
    print(f'{si_form(value, round_to_decimal_places=3) = }')
    print(f'{engineering_form(value, round_to_decimal_places=0) = }')
    print(f'{sif(value, "V") = }')
    print(f'{engf(value, "V") = }')

if __name__ == '__main__':
    try:
        _test()
    except Exception as e:
        raise e
