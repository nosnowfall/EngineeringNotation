# Engineering Notation

This Python class provides functionality to convert numeric values into engineering notation. Engineering notation is a way of representing numbers in scientific notation but the exponent is a power of 3, allowing numbers to be directly read as SI units.

## Example usage

```py
from EngineeringNotation import EngineeringNotation

# Example usage
value = 12345678.9
eng_notation = EngineeringNotation(value)

# Get the value in standard SI form (with metric prefix)
si_form = eng_notation.get_si_form()
print(si_form) # Prints: 12.35 M as in Mega

# Get the value in engineering form (with exponent)
eng_form = eng_notation.get_engieering_form()
print(eng_form) # Prints: 12.35E6 as in 12.35*10^6
```
