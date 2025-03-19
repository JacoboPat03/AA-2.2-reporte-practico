# Generador de funciones para calcular promedios ponderados
def crear_calculadora_promedio_ponderado(pesos):
    def calcular(notas):
        return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
    return calcular

calculadora = crear_calculadora_promedio_ponderado([0.3, 0.4, 0.3])
notas = [85, 90, 78]
print("Promedio ponderado:", calculadora(notas))