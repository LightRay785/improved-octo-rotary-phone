def fib(n):
  a = 0
  b = 1
  if n == 1 or n == 2:
    return b
  elif n <= 0:
    return 'Invalid Input'
  else:
    for i in range(2,n+1):
      c = a + b
      a = b
      b = a
print(fib(10))
