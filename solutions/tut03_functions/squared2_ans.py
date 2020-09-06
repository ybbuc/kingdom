def square(n):  
  # ** Returns the square of a number
  squared = n**2
  statement ='%d squared is %d.' %(n, squared)
  return statement

n = int(input('Enter a number: '))
print(square(n))


