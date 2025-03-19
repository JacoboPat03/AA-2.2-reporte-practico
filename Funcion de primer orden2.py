# Función para validar si un estudiante aprobó una materia
def aprobado(nota):
    return nota >= 70

# Solicitar al usuario que ingrese la nota final
try:
    nota_final = float(input("Ingrese la nota final del estudiante: "))
    print("Aprobado:", aprobado(nota_final))
except ValueError:
    print("Error: Por favor, ingrese un número válido.")