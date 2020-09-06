product = 0
def multiply(num1, num2):
   #local variable
   product = num1 * num2 
   statement ='The local variable is %d.' %product
   return statement

print(multiply(10, 20))
print('However, the global variable is still %d.' %product)
