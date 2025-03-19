# Filtrar tareas pendientes 
tareas = [("Tarea 1: Exposicion", True), ("Tarea 2: Cuadro comparativo", True), ("Tarea 3:reporte de practicas", False)]
tareas_pendientes = list(filter(lambda x: not x[1], tareas))
print("Tareas pendientes:", tareas_pendientes)
