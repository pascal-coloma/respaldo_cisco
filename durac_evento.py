# La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado
# expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). 
# El resultado debe ser mostrado en la consola.
# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

hour = int(input("Hora de inicio (horas): ")) 
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))



# convertir hrs a minutos sumar los minutos que dura el evento, teniendo eso, lo convierto a horas 
# el resto del minuto de horas por horas 
