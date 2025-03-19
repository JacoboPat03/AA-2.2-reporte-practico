# Notificar cuando se complete la descarga de un recurso
def descargar_recurso(url, callback):
    print(f"Descargando {url}...")
    # Simulación de descarga
    print("Descarga completada.")
    callback()

def notificar_descarga():
    print("Notificación: El recurso ha sido descargado.")

descargar_recurso("http://ejemplo.com/recurso", notificar_descarga)