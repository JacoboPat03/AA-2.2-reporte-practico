#ejercicio 1 ordenar un cafe para el grupo ISC

def preparar_cafe():
    return "cafe"
def ordenar_cafe(num_tazas):
    tazas_cafe =[preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe
cafe_grupo_a = ordenar_cafe(int (input ('Ingresa tu orden: ')))
print(cafe_grupo_a)

