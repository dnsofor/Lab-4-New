def is_triangle(a,b,c):
   """Return True if a, b, and c can form a triangle.
   >>> is_triangle(3, 4, 5)
   True
   >>> is_triangle(2, 3, 10)
   False
   """
   return a + b > c and a + c > b and b + c > a
