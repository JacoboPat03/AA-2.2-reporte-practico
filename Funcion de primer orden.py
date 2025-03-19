# Calcular el promedio de notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

notas_estudiante = [75, 100, 88, 95]
print("Promedio:", calcular_promedio(notas_estudiante))