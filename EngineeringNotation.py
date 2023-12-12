class EngineeringNotation():
    si_prefixes = {
        -30: 'y',
        -27: 'r',
        -24: 'y',
        -21: 'z',
        -18: 'a',
        -15: 'f',
        -12: 'p',
        -9: 'n',
        -6: 'μ',
        -3: 'm',
        0: None,
        3: 'k',
        6: 'M',
        9: 'G',
        12: 'T',
        15: 'P',
        18: 'E',
        21: 'Z',
        24: 'Y',
        27: 'R',
        30: 'Q',
    }
    
    def __init__(self, number):
        self.value = round(number, 7)
        self.engineering_exponent = self._get_engineering_exponent()
        self.mantissa = round(self.value / 10 ** self.engineering_exponent, 2)
        self.prefix = EngineeringNotation.si_prefixes.get(self.engineering_exponent)
    
    def _get_engineering_exponent(self):
        if self.value == 0:
            return 0
        exponent = int(math.log10(abs(self.value)))
        while exponent % 3 != 0:
            exponent -= 1
        return exponent
    
    def get_si_form(self):
        return f'{self.mantissa} {self.prefix}' if self.prefix is not None else f'{self.mantissa}'
    
    def get_engieering_form(self):
        return f'{self.mantissa}E{self.engineering_exponent}'