#  Aplicar un descuento a notas
def aplicar_descuento(descuento):
    def calcular_nota_final(nota):
        return nota * (1 - descuento)
    return calcular_nota_final

descuento_10 = aplicar_descuento(0.1)
nota_final = descuento_10(90)
print("Nota con descuento:", nota_final)