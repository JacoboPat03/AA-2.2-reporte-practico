def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"
def preparar_hotdog():
    return "🌭"
def ordenar_alimentos(preparar, num_porciones):
    porciones_A  = [preparar() for _ in range(num_porciones)]
    return porciones_A
cafe_grupo_A = ordenar_alimentos(preparar_pizza,int(input("Numero de porciones: ")))
print(cafe_grupo_A)

cafe_grupo_B = ordenar_alimentos(preparar_hamburguesa,int(input("Numero de porciones: ")))
print(cafe_grupo_B)

cafe_grupo_C = ordenar_alimentos(preparar_hotdog,int(input("Numero de porciones: ")))
print(cafe_grupo_C)