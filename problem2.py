def divisible_by_m(n,m):
  """
  Return True if n is divisible by m, and False otherwise.

  >>> divisible_by_m(3,2)
  False
  >>> divisible_by_m(0,4)
  True
  >>> divisible_by_m(-6, 2)
  True
  >>> divisible_by_m(10, 5)
  True
  >>> divisible_by_m(7, 3)
  False
  >>> divisible_by_m(5, 0)
  False
  """
  return n % m == 0
