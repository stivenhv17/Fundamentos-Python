# Se crean las variables con los valores dados por el laboratorio.
kilometers = 12.25
miles = 7.38

# hacemos la conversión de millas a kilómetros, 1 milla equivale aproximadamente a 1.61 kilómetros y por eso multiplicamos las millas por 1.61.
miles_to_kilometers = miles * 1.61

# Hacemos la conversión de kilómetros a millas y para regresar a millas dividimos entre 1.61.
kilometers_to_miles = kilometers / 1.61

# round(valor, 2) redondea el resultado a dos decimales y print() permite mostrar texto y variables al mismo tiempo.

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")