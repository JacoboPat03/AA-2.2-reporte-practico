# Ordenar una lista de estudiantes por su promedio
estudiantes = [("Guillermo", 75), ("Wilbert", 92), ("Santos", 75)]
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1], reverse=True)
print("Estudiantes ordenados:", estudiantes_ordenados)