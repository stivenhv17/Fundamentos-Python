# Solicitamos al usuario un valor para x.
# input() siempre devuelve texto, por eso usamos float() para convertirlo en un número decimal.
x = float(input("Ingrese el valor de x: "))

# Calculamos: y = 3x³ - 2x² + 3x - 1
# En Python la potencia se representa con ** y la multiplicación siempre debe escribirse con *

y = 3 * (x ** 3) - 2 * (x ** 2) + 3 * x - 1
print("y =", y) # Muestra el resultado