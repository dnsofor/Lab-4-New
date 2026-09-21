def if_function(condition, true_result, false_result):
  """ Boolean expression, value, value -> value
  Return true_result if condition is true and false_result otherwise

  >>> if_function(True, 2, 3)
  2
  >>> if_function(False, 2, 3)
  3
  >>> if_function(3==2, 3+2, 3-2)
  1
  >>> if_function(3>2, 3+2, 3-2)
  5 
  """
  if condition:
    return true_result
  else:
    return false_result

def with_if_statement():
  """
  >>> result = with_if_statement()
  2
  >>> print(result)
  None
  """
  if c():
    return t()
  else: 
    return f()

def with_if_function():
  """
  >>> result = with_if_function()
  1
  2
  >>> print(result)
  None
  """
  return if_function(c(), t(), f())

def c():
  """Return False.
  >>> c()
  False
  """
  return False


def t():
  """Print 1 and return 1.
  >>> t()
  1
  1
  """
  print(1)
  return 1


def f():
  """Print 2 and return 2.
  >>> f()
  2
  2
  """
  print(2)
  return 2
