import os
from PIL import Image

def recortar_borde_inferior(imagen, border_ratio):
    # Obtener el tamaño de la imagen
    width, height = imagen.size
    
    # Calcular el borde proporcional
    border_size = int(height * border_ratio)
    
    # Definir los límites del recorte (solo el borde inferior)
    left = 0
    top = 0
    right = width
    bottom = height - border_size  # Recortar solo la parte inferior
    
    # Recortar la imagen
    subimage = imagen.crop((left, top, right, bottom))
    return subimage, border_size  # También devolvemos el tamaño del borde usado

# Configuración inicial
REFERENCE_HEIGHT = 3654  # Altura de la imagen de referencia
REFERENCE_BORDER = 500  # Borde que funciona bien en la imagen de referencia
BORDER_RATIO = REFERENCE_BORDER / REFERENCE_HEIGHT  # Proporción del borde
INPUT_DIR = "healthy_images"  # Directorio de entrada

# Procesar cada imagen en el directorio de entrada
for archivo in os.listdir(INPUT_DIR):
    if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
        ruta_imagen = os.path.join(INPUT_DIR, archivo)
        imagen_original = Image.open(ruta_imagen)

        print(f"Tamaño de la imagen: {imagen_original.size}")
        print(f"Formato de la imagen: {imagen_original.format}")

        # Recortar el borde inferior proporcionalmente
        imagen_recortada, border_used = recortar_borde_inferior(imagen_original, BORDER_RATIO)

        print(f"Borde aplicado: {border_used} píxeles")

        # Guardar la imagen recortada
        save_name = f"{archivo}_processed.jpg"
        imagen_recortada.save(f"cut_full_images/{save_name}")
