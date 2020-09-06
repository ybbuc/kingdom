# functions homework
## converter.py
Write a function named converter that lets a user input a temperature in Celsius. A message should be printed stating what the temperature is in Fahrenheit.
- For example, “37 Celsius converted to Fahrenheit is 100”.
- "Celsius"=(Fahrenheit-32)×5/9

## city_names.py
Write a function called city_country that takes in the name of a city and its country.
- The function should return a string formatted like this: "Santiago, Chile"
- Call your function with at least three city-country pairs, and print the value that’s returned.

## quadratic.py
Write a function named solve_quadratic that solves a quadratic equation.
- The function should have three parameters:  a, b, and c.
- Allow user input of the function arguments (integers; do this outside of solve_quadratic)
- The function should return a string.
- Any numbers should be to two decimal places
- Four outcomes (strings) you must consider:
    - “x = 2.00” (one root:  b^2-4ac=0)
    - “x = 4.24 or 6.12” (two roots:  b^2-4ac>0)
	- “Imaginary solutions” (complex roots: b^2-4ac<0)
	- “Not a quadratic” (a=0)
- Print the result of the function outside of the function.
- You will need to import the math library to perform a square root. 
```python
import math
math.sqrt(num)
```
- It’s possible to use several returns in a function:
``` python
def example_func():
    if condition:
        return something
    elif condition:
        return something_else
    else:
        return secret

result = example_func()
```