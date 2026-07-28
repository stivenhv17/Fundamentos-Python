
# Algoritmo 1 - Calcular el puntaje total de un jugador
# Solicitamos los puntos obtenidos en cada nivel.
nivel1 = int(input("Ingrese los puntos del nivel 1: "))
nivel2 = int(input("Ingrese los puntos del nivel 2: "))
nivel3 = int(input("Ingrese los puntos del nivel 3: "))

puntaje_total = nivel1 + nivel2 + nivel3 # Sumamos los puntos de los tres niveles.
print("El puntaje total del jugador es:", puntaje_total)# Mostramos el resultado.

# ==========================================
# Algoritmo 2 - Tiempo total en segundos
# Solicitamos las horas, minutos y segundos.
horas = int(input("Ingrese las horas jugadas: "))
minutos = int(input("Ingrese los minutos jugados: "))
segundos = int(input("Ingrese los segundos jugados: "))

total_segundos = (horas * 3600) + (minutos * 60) + segundos # Convertimos todo a segundos.
print("Tiempo total jugado en segundos:", total_segundos)# Mostramos el resultado.

# ==========================================
# Algoritmo 3 - Daño total causado
# Solicitamos el daño de cada ataque.
ataque1 = float(input("Daño del ataque 1: "))
ataque2 = float(input("Daño del ataque 2: "))
ataque3 = float(input("Daño del ataque 3: "))

danio_total = ataque1 + ataque2 + ataque3 # Calculamos el daño total.
print("Daño total causado:", danio_total)# Mostramos el resultado.

# ==========================================
# Algoritmo 4 - Experiencia total ganada
# Solicitamos la experiencia obtenida en cada misión.
mision1 = int(input("Experiencia misión 1: "))
mision2 = int(input("Experiencia misión 2: "))
mision3 = int(input("Experiencia misión 3: "))

experiencia_total = mision1 + mision2 + mision3 # Sumamos la experiencia.
print("Experiencia total acumulada:", experiencia_total) # Mostramos el resultado.

# ==========================================
# Algoritmo 5 - Porcentaje de vida restante
# Solicitamos la vida máxima y la vida actual del personaje.
vida_maxima = float(input("Ingrese la vida máxima del personaje: "))
vida_actual = float(input("Ingrese la vida actual del personaje: "))

porcentaje_vida = (vida_actual / vida_maxima) * 100 # Calculamos el porcentaje de vida restante.
print("Porcentaje de vida restante:", porcentaje_vida, "%") # Mostramos el resultado.

# ==========================================
# Algoritmo 6 - Oro total recolectado
# Solicitamos el oro obtenido en cada misión.
oro1 = int(input("Ingrese el oro de la misión 1: "))
oro2 = int(input("Ingrese el oro de la misión 2: "))
oro3 = int(input("Ingrese el oro de la misión 3: "))

oro_total = oro1 + oro2 + oro3 # Sumamos todo el oro obtenido.
print("Oro total recolectado:", oro_total) # Mostramos el resultado.

# ==========================================
# Algoritmo 7 - Velocidad promedio
# Solicitamos la distancia recorrida y el tiempo.
distancia = float(input("Ingrese la distancia recorrida (km): "))
tiempo = float(input("Ingrese el tiempo empleado (horas): "))

velocidad = distancia / tiempo# Calculamos la velocidad promedio.
print("Velocidad promedio:", velocidad, "km/h")# Mostramos el resultado.

# ==========================================
# Algoritmo 8 - Costo total de mejoras
# Solicitamos el costo de las tres mejoras.
mejora1 = float(input("Costo de la mejora 1: "))
mejora2 = float(input("Costo de la mejora 2: "))
mejora3 = float(input("Costo de la mejora 3: "))

costo_total = mejora1 + mejora2 + mejora3# Sumamos el costo de todas las mejoras.
print("Costo total de las mejoras:", costo_total)# Mostramos el resultado.

# ==========================================
# Algoritmo 9 - Tiempo restante de una misión
# Solicitamos el tiempo total de la misión y el tiempo transcurrido.
tiempo_total = float(input("Ingrese el tiempo total de la misión (minutos): "))
tiempo_transcurrido = float(input("Ingrese el tiempo transcurrido (minutos): "))

tiempo_restante = tiempo_total - tiempo_transcurrido# Calculamos el tiempo restante.
print("Tiempo restante para completar la misión:", tiempo_restante, "minutos")# Mostramos el resultado.

# ==========================================
# Algoritmo 10 - Nivel promedio del equipo
# Solicitamos el nivel de cada jugador.
jugador1 = int(input("Ingrese el nivel del jugador 1: "))
jugador2 = int(input("Ingrese el nivel del jugador 2: "))
jugador3 = int(input("Ingrese el nivel del jugador 3: "))

promedio = (jugador1 + jugador2 + jugador3) / 3 # Calculamos el promedio de los niveles.
print("Nivel promedio del equipo:", promedio)# Mostramos el resultado.

# ==========================================
# Algoritmo 11 - Daño crítico
# Solicitamos el daño base y el multiplicador crítico.
danio_base = float(input("Ingrese el daño base del ataque: "))
multiplicador = float(input("Ingrese el multiplicador crítico: "))

danio_critico = danio_base * multiplicador# Calculamos el daño crítico.
print("Daño crítico del ataque:", danio_critico)# Mostramos el resultado.

# ==========================================
# Algoritmo 12 - Tiempo total en horas y minutos
# Solicitamos el tiempo total jugado en minutos.
minutos_totales = int(input("Ingrese el tiempo total jugado en minutos: "))

horas = minutos_totales // 60# Calculamos las horas usando división entera.
minutos = minutos_totales % 60# Calculamos los minutos restantes usando el operador módulo.
print("Tiempo jugado:", horas, "hora(s) y", minutos, "minuto(s)")# Mostramos el resultado.

# ==========================================
# Algoritmo 13 - Porcentaje de misiones completadas
# Solicitamos el número total de misiones y las completadas.
total_misiones = int(input("Ingrese el número total de misiones: "))
misiones_completadas = int(input("Ingrese el número de misiones completadas: "))

porcentaje = (misiones_completadas / total_misiones) * 100# Calculamos el porcentaje de misiones completadas.
print("Porcentaje de misiones completadas:", porcentaje, "%")# Mostramos el resultado.

# ==========================================
# Algoritmo 14 - Costo total de objetos comprados
# Solicitamos el costo de cada objeto.
objeto1 = float(input("Ingrese el costo del objeto 1: "))
objeto2 = float(input("Ingrese el costo del objeto 2: "))
objeto3 = float(input("Ingrese el costo del objeto 3: "))

costo_total = objeto1 + objeto2 + objeto3# Sumamos el costo de los tres objetos.
print("Costo total de los objetos:", costo_total)# Mostramos el resultado.

# ==========================================
# Algoritmo 15 - Tiempo promedio de una partida
# Solicitamos la duración de las tres partidas.
partida1 = float(input("Ingrese el tiempo de la partida 1 (minutos): "))
partida2 = float(input("Ingrese el tiempo de la partida 2 (minutos): "))
partida3 = float(input("Ingrese el tiempo de la partida 3 (minutos): "))

promedio = (partida1 + partida2 + partida3) / 3# Calculamos el promedio de tiempo.
print("Tiempo promedio de las partidas:", promedio, "minutos")# Mostramos el resultado.

# ==========================================
# Algoritmo 16 - Porcentaje de enemigos derrotados
# Solicitamos el número total de enemigos y los derrotados.
total_enemigos = int(input("Ingrese el número total de enemigos: "))
enemigos_derrotados = int(input("Ingrese el número de enemigos derrotados: "))

porcentaje = (enemigos_derrotados / total_enemigos) * 100# Calculamos el porcentaje de enemigos derrotados.
print("Porcentaje de enemigos derrotados:", porcentaje, "%")# Mostramos el resultado.