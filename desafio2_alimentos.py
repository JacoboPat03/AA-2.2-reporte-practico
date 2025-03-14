def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"
def preparar_hotdog():
    return "🌭"
def ordenar_alimentos(preparar, num_porciones):
    porciones_A  = [preparar() for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)

    return porciones_A, bonus

def calcular_bonus(num):
    if(num > 2):
        return "coca gratis"
    else:
        return ""

print(ordenar_alimentos(preparar_pizza, 2))
print(ordenar_alimentos(preparar_hamburguesa, 5))
print(ordenar_alimentos(preparar_hotdog,3))
