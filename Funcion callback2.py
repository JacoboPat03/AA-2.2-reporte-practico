#  Ejecutar una acción después de enviar un formulario
def enviar_formulario(datos, callback):
    print("Enviando formulario...")
    # Simulación de envío
    print("Formulario enviado.")
    callback()

def mostrar_mensaje_exito():
    print("Éxito: El formulario se envió correctamente.")

enviar_formulario({"nombre": "Cobos"}, mostrar_mensaje_exito)