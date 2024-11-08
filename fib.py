"""
Generador de números de Fibonacci
Dado una posición, la función devuelve el número de Fibonacci en esa posición de la secuencia.
El número cero en la secuencia de Fibonacci es 0. El primer número es 1
Los números negativos no son aceptados
"""

def fibonacci(position):
  # Error en caso de valores negativos.
  if(position < 0): raise ValueError("Invalid input")

  # (INCLUIR) caso base cuando tenemos valor 0.
  if(position == 0): return 0

  # Caso base cuando tenemos valor 1 y 2.
  if(position == 1 or position == 2): return 1
  
  # Caso recursivo.
  return fibonacci(position - 1) + fibonacci(position - 2)
  