def preparar_hotcakes():
    return "🥞"
def ordenar_hc(num_piezas):
    piezas_hc  =[preparar_hotcakes() for _ in range(num_piezas)]
    return piezas_hc
hotcakes_para_familia = ordenar_hc (int (input ('Ingresa el numero de integrantes de tu familia: ')))
print(hotcakes_para_familia)