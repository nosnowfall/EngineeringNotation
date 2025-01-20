# Engineering Notation

This Python module provides functionality to convert numeric values into engineering notation. Engineering notation is a way of representing numbers in scientific notation but the exponent is a power of 3, allowing numbers to be directly read as SI units.

## Example usage

```py
from EngineeringNotation import *

value = 12345678.9

# Get the value in standard SI form (with metric prefix)
si_value = si_form(value)
# sif(value) is an alias of si_form(value)
print(si_value) # Prints: 12.35 M as in Mega

# Get the value in engineering form (with exponent)
eng_value = engineering_form(value)
# engf(value) is an alias of engineering_form(value)
print(eng_value) # Prints: 12.35E+6 as in 12.35*10^6
```
## Formatting Units and Significant Digits
Both formatters are capable of incorporating units and rounding to a select number of digits after the decimal point. For example:
```
print(si_value(value, 'V', 3)) # Prints: 12.346 MV
```
