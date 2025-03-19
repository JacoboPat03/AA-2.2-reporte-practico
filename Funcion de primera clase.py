# Ordenar una lista de proyectos por fecha
proyectos = [("Proyecto A", "2024-10-01"), ("Proyecto B", "2024-03-15"), ("Proyecto C", "2024-11-20")]
proyectos_ordenados = sorted(proyectos, key=lambda x: x[1])
print("Proyectos ordenados:", proyectos_ordenados)

